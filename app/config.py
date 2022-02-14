# import secrets

# class Base:
#     FLASK_APP= "main.py"
#     SQLALCHEMY_TRACK_MODIFICATION=False
#     SECRET_KEY=secrets.token_hex(16)
    
    
    
# class Development(Base):
#     FLASK_ENV = "development"
#     # DATABASE = os.environ.get('DATABASE')
#     DATABASE = ""
#     POSTGRES_USER= ""
#     POSTGRES_PASSWORD=""
#     SQLALCHEMY_DATABASE_URI="postgresql+psycopg2://moringa:1234@localhost/pitchess"
    
    
    
# class staging(Base):
#     DATABASE = ""
#     POSTGRES_USER= ""
#     POSTGRES_PASSWORD=""
#     SQLALCHEMY_DATABASE_URI=""

    
# class production(Base):
#         DATABASE = ""
#         POSTGRES_USER= ""
#         POSTGRES_PASSWORD=""
#         SQLALCHEMY_DATABASE_URI=""

  
import os
os.urandom(24)

class Config:
    SECRET_KEY = 'mysecretket'
    # SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://moringa:lilian@localhost/apostgre'

    @staticmethod
    def init_app(app):
        pass


class ProdConfig(Config):
    '''
    Production  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI =os.environ.get('SQLALCHEMY_DATABASE_URI')
  


class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    DEBUG = True



        
