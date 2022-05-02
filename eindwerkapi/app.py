from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
# from flask_mail import Mail
from eindwerkapi.database.db import initialize_db
from flask_restful import Api
from eindwerkapi.resources.errors import errors
from eindwerkapi.blauwdruk import simple_page
# from dotenv import load_dotenv


app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
        "host": "mongodb+srv://m001-student:m001-mongodb-basics@sandbox.pdczs.mongodb.net/eindwerk?retryWrites=true&w=majority"
}
app.config["JWT_SECRET_KEY"] = "super-secret"
app.config["MAIL_SERVER"] = "localhost"
app.config["MAIL_PORT"] = "1025"
app.config["MAIL_USERNAME"] = "support@product-bag.com"
app.config["MAIL_PASSWORD"] = ""

# mail = Mail(app)
from eindwerkapi.resources.routes import initialize_routes
app.register_blueprint(simple_page, url_prefix="/ui")

api = Api(app, errors=errors)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)




initialize_db(app)
# app.register_blueprint(products)
initialize_routes(api)

