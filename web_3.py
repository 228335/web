from flask import Flask
import json
from flask import render_template
from flask import url_for
from flask import redirect
from loginform import LoginForm
app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    user = "Ученик Яндекс.Лицея"
    return render_template('index.html', title='Домашняя страница',
                           username=user)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')