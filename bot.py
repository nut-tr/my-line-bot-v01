from flask import Flask, request, abort
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import (MessageEvent, TextMessage, TextSendMessage,)

app = Flask(__name__)

line_bot_api = LineBotApi('GZofvtpv24/IiSD+lpJlMf/uOpV5FN+DF7ifXllZ9afzGnSf1vb0XM4YGz9HK83XI6OUTeGG6GrePdGrVqhtiht6rwQSFKw9bxMJyvBUjuCcDjNSyV8Dko8fn9MnhJNo7LfFqLLth4XsGqYq02vUjgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('4ea18ea182e0c8e6d22b624cf40521ad')

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/webhook", methods=['POST'])
def webhook():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'
    

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()
