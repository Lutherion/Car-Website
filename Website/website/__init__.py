from flask import Flask

app = Flask(__name__)

import website.forms

currentUser = 'None'

app.config['SECRET_KEY'] = 'koskdfokowpeiropwieroiteroito494'