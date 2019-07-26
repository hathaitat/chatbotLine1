#เป็นไฟล์เอาไว้เชื่อมต่อ ที่เอาไวเชื่อม URL
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

#ใส่ token ของ Line
line_bot_api = LineBotApi('InzvvC6224QOYMDG9pzPoTUk8zVKwVHv1XaCc/vjz5ebOUrdod8QOLfvRzofLiNqqEVDqV7tG8VDnpxLo8kLAQ0u3YVGKphURTLkpVIGrzuLXRQaYv/o19YS0GLz4bXKkafZV0iIPI6P1tC+flLnQAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('fb59bf1fa17d60c08da1ac2619a0e0f7')


@app.route("/whbell/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature'] #request.headers????

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)  #logger 

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run(host='0.0.0.0')

#ถ้า test ใส่ 0.0.0.0 ไม่ได้ ต้องเป็น 127.0.0.1 