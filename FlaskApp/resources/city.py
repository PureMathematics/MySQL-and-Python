from database.models import City
from flask import Response, request
from flask_restful import Resource

class CitiesApi(Resource):
    def get(self):
        cities = City.objects().to_json()
        return Response(cities, mimetype="application/json", status=200)

    def post(self):
        body = request.get_json()
        city = City(**body).save()
        post_id = city.post_id
        return {'post_id': str(post_id)}, 200
    
class CityApi(Resource):
    def put(self, post_id):
        body = request.get_json()
        City.objects.get(post_id=post_id).update(**body)
        return '', 200

    def delete(self, post_id):
        city = City.objects.get(post_id=post_id).delete()
        return '', 200

    def get(self, post_id):
        cities = City.objects.get(post_id=post_id).to_json()
        return Response(cities, mimetype="application/json", status=200)
