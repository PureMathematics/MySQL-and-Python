from flask import Flask, request, Response
from database.db import initialize_db

from resources.city import cities
app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
 'host': 'mongodb://localhost/city-list'
}
db = initialize_db(app)
app.register_blueprint(cities)

#APIs
@app.route("/")
def main():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(port=5002,debug=True)