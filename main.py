from flask import Flask


app = Flask(__name__)

#rotas
from views import *

if __name__ == "__main__" :
    app.run()