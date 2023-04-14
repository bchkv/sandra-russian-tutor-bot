import logging
from telegram import Update
from telegram.ext import filters, ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler
from chat_gpt import chat_gpt_response
import os

SandraRussianTutorBot_TOKEN = os.environ["SandraRussianTutorBot_TOKEN"]

# Set up log formatting
log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

# Configure the file handler to write logs to a file
file_handler = logging.FileHandler('sandra_russian_tutor_bot.log')
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(logging.Formatter(log_format))

# Configure the stream handler to output logs to the console
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)
stream_handler.setFormatter(logging.Formatter(log_format))

# Configure the root logger with both handlers
logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(file_handler)
logger.addHandler(stream_handler)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="I'm a bot, please talk to me!"
    )


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)


async def chat_gpt(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = update.message.text
    chat_gpt_output = await chat_gpt_response(user_input)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=chat_gpt_output)


if __name__ == '__main__':
    application = ApplicationBuilder().token(SandraRussianTutorBot_TOKEN).build()

    # Listens to the command '/start' and runs the function 'start()'
    start_handler = CommandHandler('start', start)
    chat_gpt_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), chat_gpt)

    application.add_handler(start_handler)
    application.add_handler(chat_gpt_handler)

    application.run_polling()