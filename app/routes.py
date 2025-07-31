from app import app
from flask import request
from app.handlers import generate_reply

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    user_message = data.get('message', '')
    response = generate_reply(user_message)
    return {'reply': response}
