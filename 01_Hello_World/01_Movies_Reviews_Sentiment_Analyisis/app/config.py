
class Config:
    ENV = "production"
    TESTING = False
    DEBUG = False

class Production(Config):
    pass

class Development(Config):
    DEBUG = True
    ENV = "development"

class Testing(Config):
    TESTING = True
    ENV = "testing"