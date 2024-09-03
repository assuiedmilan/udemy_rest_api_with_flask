from rest_api_with_flask.api.rest_api import RestApi
from rest_api_with_flask.resources import stores
from rest_api_with_flask.resources.status_codes import codes

app = RestApi.create_app()


@RestApi.rest_app().get('/stores')  # http://127.0.0.1:5000/stores
def get_stores():
    return {'stores': stores.STORES}


@RestApi.rest_app().post('/stores')
def add_stores():
    received_data = RestApi.request_json()

    if stores.NAME_KEY not in received_data:
        return {'message': 'The store name is required'}, codes.BAD_REQUEST

    name = received_data[stores.NAME_KEY]

    if name in [store[stores.NAME_KEY] for store in stores.STORES]:
        return {'message': 'Store already exists'}, codes.BAD_REQUEST

    items = received_data[stores.ITEMS_KEY] if stores.ITEMS_KEY in received_data else list()

    if items:
        for item in items:
            if not stores.validate_item(item):
                return {'message': 'An item must have a name and a price'}, codes.BAD_REQUEST

    new_store = {stores.NAME_KEY: name, stores.ITEMS_KEY: items}

    stores.STORES.append(new_store)
    return stores.STORES, codes.CREATED
