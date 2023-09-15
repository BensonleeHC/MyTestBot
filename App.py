"""
https://asia-east1-linebot-mytestbot.cloudfunctions.net/App/callback
"""

from flask import Flask, request, abort
import configparser
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
config=configparser.ConfigParser()
config.read('config.ini')

app = Flask(__name__)

        
api_client = ApiClient(Configuration(access_token=config.get('line_bot', 'Channel_Token')))
handler = WebhookHandler(config.get('line_bot', 'Channel_Secret'))
#line_bot_api = MessagingApi(config.get('line_bot', 'Channel_Token'))
line_bot_api = MessagingApi(api_client)

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info(json.dumps(body, sort_keys=True,indent=4))
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'
"""
Main Message handler. add code here.
"""
@handler.add(MessageEvent, message=TextMessageContent)
def handle_message(event):
    app.logger.info("handle Message Entry")
    
    ##Corporate User only, no API permission
    #mark_messages_as_read_request = {"chat":"userId":event.source.user_id}}
    #line_bot_api.mark_messages_as_read(mark_messages_as_read_request)

    line_bot_api.reply_message_with_http_info(
        ReplyMessageRequest(
            reply_token=event.reply_token,
            messages=[TextMessage(text=event.message.text)]
        )
    )

if __name__ == "__main__":
    app.run(debug=True,port=8000)
