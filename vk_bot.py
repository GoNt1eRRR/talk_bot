import os
import random
from environs import env
from google.cloud import dialogflow_v2 as dialogflow
import vk_api as vk
from vk_api.longpoll import VkLongPoll, VkEventType


def detect_intent_texts(project_id, session_id, text, language_code="ru"):
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)

    text_input = dialogflow.TextInput(text=text, language_code=language_code)
    query_input = dialogflow.QueryInput(text=text_input)

    response = session_client.detect_intent(
        request={"session": session, "query_input": query_input}
    )

    if response.query_result.intent.is_fallback:
        return None

    return response.query_result.fulfillment_text


def answer_with_dialogflow(event, vk_api):
    response_text = detect_intent_texts(PROJECT_ID, event.user_id, event.text)
    if response_text:
        vk_api.messages.send(
            user_id=event.user_id,
            message=response_text,
            random_id=random.randint(1, 1000)
        )


if __name__ == "__main__":
    env.read_env()

    PROJECT_ID = env("PROJECT_ID")
    CREDENTIALS_PATH = env("GOOGLE_APPLICATION_CREDENTIALS")
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = CREDENTIALS_PATH
    TOKEN = env("VK_TOKEN")

    vk_session = vk.VkApi(token=TOKEN)
    vk_api = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)

    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            answer_with_dialogflow(event, vk_api)