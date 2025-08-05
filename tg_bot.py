import os
from environs import env
from google.cloud import dialogflow_v2 as dialogflow

from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext


def start(update: Update, context: CallbackContext):
    update.message.reply_text("Здравствуйте")


def detect_intent_text(project_id, session_id, text, language_code='ru'):
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)

    text_input = dialogflow.TextInput(text=text, language_code=language_code)
    query_input = dialogflow.QueryInput(text=text_input)

    response = session_client.detect_intent(
        request={"session": session, "query_input": query_input}
    )

    return response.query_result.fulfillment_text


def echo(update: Update, context: CallbackContext):
    text = update.message.text
    user_id = str(update.effective_user.id)

    response_text = detect_intent_text(
        project_id=env("PROJECT_ID"),
        session_id=user_id,
        text=text
    )

    update.message.reply_text(response_text)


def main():
    env.read_env()

    TOKEN = env("TG_TOKEN")
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = env("GOOGLE_APPLICATION_CREDENTIALS")

    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
