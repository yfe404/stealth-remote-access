import os
import subprocess
import logging
from dotenv import load_dotenv
from github import Github

from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

load_dotenv()

GIST_ID = os.environ.get("GIST_ID")
TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")


def get_gist_content(gist, filename):
    # Then play with your Github objects:
    return gist.files[filename].content


def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text("Hi!")


def execute(update, context):
    """Execute the content of the gist."""
    g = Github()

    gist = g.get_gist(GIST_ID)

    gist_content = get_gist_content(gist, "commands.txt")

    with open("script.sh", "w") as f:
        for line in gist_content.split("\n"):
            if line.startswith("#") and line.endswith(";"):
                f.write(line[1:-1] + "\n")

    result = subprocess.run(["sh", "script.sh"], stdout=subprocess.PIPE)

    update.message.reply_text(result.stdout.decode("utf-8"))


if __name__ == "__main__":

    updater = Updater(TELEGRAM_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    logging.basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=logging.DEBUG,
    )

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("exec", execute))

    updater.start_polling()
    updater.idle()
