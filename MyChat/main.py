from flask import Flask, request, render_template
from datetime import datetime
import json

app = Flask(__name__)

db_file = './data/db.json'  # way
json_db = open(db_file, 'rb')  # open file
data = json.load(json_db)  # load data from file
messages_list = data['messages_list']  #


def save_messages():  # save message to file
    data = {
        'messages_list': messages_list,
    }
    json_db = open(db_file, 'w')  # open file to write
    json.dump(data, json_db)  # write data to file


def print_message(message):
    print(f'[{message["sender"]}]: {message["text"]}/ {message["date"]}')
    print('-' * 37)


def add_message(name, txt):
    message = {
        'text': txt,
        'sender': name,
        'date': datetime.now().strftime('%H:%M')

    }
    messages_list.append(message)


@app.route('/')
def index_page():
    return 'Hello! welcome to MyChat!'


@app.route('/get_messages')
def get_messages():
    return {'messages': messages_list}


@app.route('/send_message')
def send_message():
    name = request.args['name']
    text = request.args['text']
    if len(name) > 20:
        return 'error. too many symbols'
    if len(name) < 5:
        return 'error. not enough symbols'
    if len(text) > 500 or len(text) < 1:
        return 'error'

    add_message(name, text)
    save_messages()  # save all messages to file
    return 'ok'


# Visual
@app.route('/form')
def form():
    return render_template('form.html')


app.run(host='0.0.0.0', port=80)
