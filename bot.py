import logging
from config import TOKEN_TELEGRAM
from telegram import Update
from telegram.ext import filters, ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler
from chat_gpt import chat_gpt_response

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


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
    application = ApplicationBuilder().token(TOKEN_TELEGRAM).build()

    # Listens to the command '/start' and runs the function 'start()'
    start_handler = CommandHandler('start', start)
    chat_gpt_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), chat_gpt)

    application.add_handler(start_handler)
    application.add_handler(chat_gpt_handler)

    application.run_polling()