from flask import Flask

DEBUG = True
SECRET_KEY = 'asdsa34543fjkb@h33k566786as@cavsx345acv34sc'

app = Flask(__name__)
app.config.from_object(__name__)
