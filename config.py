class Config:
    SECRET_KEY = "your_secret_key"
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://root:123456@localhost/sales_inventory"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
