from rest_api_with_flask.api.rest_api import RestApi
from rest_api_with_flask.resources import stores

app = RestApi.create_app()


@RestApi.rest_app().get('/stores')  # http://127.0.0.1:5000/stores
def get_stores():
    return {'stores': stores.STORES}
