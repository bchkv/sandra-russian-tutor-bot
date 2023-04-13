from flask import Flask, request
import bot
import threading

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, this is the homepage of your bot!'

def start_bot():
    bot.main()

if __name__ == "__main__":
    thread = threading.Thread(target=start_bot)
    thread.start()
    app.run()
