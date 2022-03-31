from flask import Flask, render_template
import datetime

app = Flask(__name__)


@app.route("/")
def index():
    current_year = datetime.datetime.now().year
    return render_template("index.html", year=current_year, variavel_index="Vamos ver se isto é o index")

@app.route("/sobre_mim")
def sobre():
    current_year = datetime.datetime.now().year
    return render_template("sobre.html", year=current_year, variavel_sobre="O meu nome é SmartNinja")


if __name__ == '__main__':
    app.run(use_reloader=True)

app.run()