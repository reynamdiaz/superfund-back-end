from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os
# from flask_cors import CORS

db = SQLAlchemy()
migrate = Migrate()
load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost:5432/superfund_development'
    # Import models here for Alembic setup
    # from app.models.ExampleModel import ExampleModel
    from app.models.superfund_site import superfund_site
 

    db.init_app(app)
    migrate.init_app(app, db)

    # from .routes import superfund_bp
    # app.register_blueprint(superfund_bp)

    


    # CORS(app)
    return app
