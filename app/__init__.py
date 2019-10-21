#coding=UTF-8
#from flask_sqlalchemy import SQLAlchemy
from flask import Flask
#from flask_bootstrap import Bootstrap
import logging
#from app.api_1_0.utils import set_constraint_name
#db=SQLAlchemy(metadata=MetaData(naming_convention=set_constraint_name()))

#db=SQLAlchemy()
#bootstrap=Bootstrap()

logger_root=logging.getLogger(__name__)
logger_root.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s %(message)s")
handler = logging.FileHandler('output.log')
handler.setFormatter(formatter)
logger_root.addHandler(handler)


def create_app():
    app=Flask(__name__)
    app.config.from_object('config')
    #db.init_app(app)
    #bootstrap.init_app(app)
    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint)
    return app