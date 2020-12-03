from .city import CitiesApi, CityApi

def initialize_routes(api):
    api.add_resource(CitiesApi, '/cities')
    api.add_resource(CityApi, '/cities/<post_id>')