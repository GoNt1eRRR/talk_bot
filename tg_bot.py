import os
from environs import env

from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

from dialogflow_helpers import detect_intent_text


def start(update: Update, context: CallbackContext):
    update.message.reply_text("Здравствуйте")


def echo(update: Update, context: CallbackContext, project_id):
    text = update.message.text
    user_id = f"tg-{update.effective_user.id}"

    response_text = detect_intent_text(
        project_id=project_id,
        session_id=user_id,
        text=text
    )

    update.message.reply_text(response_text)


def main():
    env.read_env()

    token = env("TG_TOKEN")
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = env("GOOGLE_APPLICATION_CREDENTIALS")
    project_id = env("PROJECT_ID")

    updater = Updater(token, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(
        MessageHandler(
            Filters.text & ~Filters.command,
            lambda update, context: echo(update, context, project_id)
        )
    )

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
