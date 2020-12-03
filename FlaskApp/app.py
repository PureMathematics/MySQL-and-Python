from flask import Flask, request, Response, render_template
from database.db import initialize_db
from flask_restful import Api
from resources.routes import initialize_routes
app = Flask(__name__)
api = Api(app)
app.config['MONGODB_SETTINGS'] = {
 'host': 'mongodb://localhost/city-list'
}
db = initialize_db(app)
initialize_routes(api)


#APIs
@app.route("/", methods=['GET'])
def main():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(port=5002,debug=True)