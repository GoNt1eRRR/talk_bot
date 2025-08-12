import os
import random
from environs import env
import vk_api as vk
from vk_api.longpoll import VkLongPoll, VkEventType

from dialogflow_helpers import detect_intent_text


def answer_with_dialogflow(event, vk_api, project_id):
    session_id = f"vk-{event.user_id}"
    response_text = detect_intent_text(project_id, session_id, event.text, allow_fallback=False)

    if response_text:
        vk_api.messages.send(
            user_id=event.user_id,
            message=response_text,
            random_id=random.randint(1, 1000)
        )


if __name__ == "__main__":
    env.read_env()

    project_id = env("PROJECT_ID")
    credentials_path = env("GOOGLE_APPLICATION_CREDENTIALS")
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credentials_path
    token = env("VK_TOKEN")

    vk_session = vk.VkApi(token=token)
    vk_api = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)

    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            answer_with_dialogflow(event, vk_api, project_id)