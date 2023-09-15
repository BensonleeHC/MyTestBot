#app.py
from flask import Flask, request, abort
import json
from linebot.v3 import (
    WebhookHandler
)
from linebot.v3.exceptions import (
    InvalidSignatureError
)
from linebot.v3.messaging import (
    Configuration,
    ApiClient,
    MessagingApi,
    ReplyMessageRequest,
    TextMessage
)
from linebot.v3.webhooks import (
    MessageEvent,
    TextMessageContent
)

app = Flask(__name__)

#line_bot_api = LineBotApi('V1PN/jDzCSzgyLhCjLrstxx0uSwiiItchaIjjM+C14GXlGCNISZ8vqBBTsTpbo5iLsQYxCehkNh34eIGHboSDu1CH/gf8cW8E2RQycLctGjdNs6XCvD7FLvWZbNLSqI8jqP5HHbOezy/osEyA6AJsAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('934b33388a3daae4f055524f2e08cb88')
LineMessagingApi = MessagingApi('V1PN/jDzCSzgyLhCjLrstxx0uSwiiItchaIjjM+C14GXlGCNISZ8vqBBTsTpbo5iLsQYxCehkNh34eIGHboSDu1CH/gf8cW8E2RQycLctGjdNs6XCvD7FLvWZbNLSqI8jqP5HHbOezy/osEyA6AJsAdB04t89/1O/w1cDnyilFU=')

@app.route("/callback", methods=['POST'])
def callback():
    print("callback entry")
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    #app.logger.info("Request body: " + body)
    print(json.dumps(body, sort_keys=True,indent=4))
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

def SecretMsg():
    print("SecretMsg received")
    return
##Main Message handler. add code here.
##
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    text1 = "this is handle message"
    #text2 = "you have message me this message : "+ event.message.text

    if(event.message.text == "5356"):
        SecretMsg()

    with ApiClient(configuration) as api_client:
        line_bot_api = MessagingApi(api_client)
        line_bot_api.reply_message_with_http_info(
            ReplyMessageRequest(
                reply_token=event.reply_token,
                messages=[TextMessage(text=text1)]
            )
        )

if __name__ == "__main__":
    app.run(debug=True,port=8000)
