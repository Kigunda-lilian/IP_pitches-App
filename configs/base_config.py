import secrets

class Base:
    FLASK_APP= "main.py"
    SQLALCHEMY_TRACK_MODIFICATION=False
    SECRET_KEY=secrets.token_hex(16)
    
    
    
    class Development(Base):
        FLASK_ENV = "development"
        # DATABASE = os.environ.get('DATABASE')
        DATABASE = ""
        POSTGRES_USER= ""
        POSTGRES_PASSWORD=""
        SQLALCHEMY_DATABASE_URI="sqlite:///tmp/pitches.db"
        
        
        class Development(Base):
            FLASK_ENV = "development"
        # DATABASE = os.environ.get('DATABASE')
        DATABASE = ""
        POSTGRES_USER= ""
        POSTGRES_PASSWORD=""
        SQLALCHEMY_DATABASE_URI="sqlite:///tmp/pitches.db"
        
        
        class staging(Base):
          DATABASE = ""
          POSTGRES_USER= ""
          POSTGRES_PASSWORD=""
          SQLALCHEMY_DATABASE_URI=""
        
        
    class production(Base):
          DATABASE = ""
          POSTGRES_USER= ""
          POSTGRES_PASSWORD=""
          SQLALCHEMY_DATABASE_URI=""
            
    