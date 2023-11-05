from os import getenv

from flask import Flask, render_template

from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect

from models import db, Product
from views.products import products_app

app = Flask(__name__)
app.register_blueprint(products_app)

config_class_name = getenv("CONFIG_CLASS", "DevelopmentConfig")
config_object = f"config.{config_class_name}"
app.config.from_object(config_object)

db.init_app(app)
migrate = Migrate(app=app, db=db)
csrf = CSRFProtect(app)


@app.get("/", endpoint="index")
def get_index():
    return render_template("index.html")


@app.get("/about/", endpoint="about")
def get_about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
