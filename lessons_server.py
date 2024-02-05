from flask import Flask
from flask import url_for
app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!!"

@app.route('/image_mars')
def return_sample_page():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Яндекс!</title>
                  </head>
                  <body>
                    <h1>Привет, Марс!</h1>
                    <img src="{url_for('static', filename='img/MARS.png')}"
                    alt="здесь должна была быть картинка, но не нашлась">
                    <h5>Жди нас, Марс!<h5>
                  </body>
                </html>"""
if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')