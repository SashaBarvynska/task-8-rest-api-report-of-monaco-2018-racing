from flasgger import Swagger
from flask import Flask
from flask_restful import Api

app = Flask(__name__)
app.json.sort_keys = False

api = Api(app)
swagger = Swagger(app)
