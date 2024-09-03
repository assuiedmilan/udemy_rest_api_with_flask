from rest_api_with_flask.api.rest_api import RestApi
from rest_api_with_flask.resources import stores
from rest_api_with_flask.resources.status_codes import codes

app = RestApi.create_app()


@RestApi.rest_app().get('/stores')  # http://127.0.0.1:5000/stores
def get_stores():
    return {'stores': stores.STORES}


@RestApi.rest_app().post('/stores')
def add_store():
    received_data = RestApi.request_json()

    if stores.NAME_KEY not in received_data:
        return {'message': 'The store name is required'}, codes.BAD_REQUEST

    name = received_data[stores.NAME_KEY]

    if name in [store[stores.NAME_KEY] for store in stores.STORES]:
        return {'message': 'Store already exists'}, codes.BAD_REQUEST

    new_store = {stores.NAME_KEY: name, stores.ITEMS_KEY: list()}

    stores.STORES.append(new_store)
    return stores.STORES, codes.CREATED


@RestApi.rest_app().post('/stores/<string:store_name>/items')
def add_items(store_name: str):
    items_list_key = "items"
    received_data = RestApi.request_json()

    if items_list_key not in received_data:
        return {'message': 'The items list is required'}, codes.BAD_REQUEST

    items_list = received_data[items_list_key]

    if not items_list:
        return {'message': 'The items list is empty'}, codes.BAD_REQUEST

    for item in received_data[items_list_key]:
        response, code = __add_item(store_name, item)

        if code != codes.CREATED:
            return response, code

    return stores.STORES, codes.CREATED


def __add_item(store_name: str, item: dict):
    if not stores.validate_item(item):
        return {'message': 'An item must have a name and a price'}, codes.BAD_REQUEST
    if store_name not in [store[stores.NAME_KEY] for store in stores.STORES]:
        return {'message': 'Store not found'}, codes.BAD_REQUEST

    item = {stores.NAME_KEY: item[stores.NAME_KEY], stores.PRICE_KEY: item[stores.PRICE_KEY]}

    for store in stores.STORES:
        if store[stores.NAME_KEY] == store_name:
            store[stores.ITEMS_KEY].append(item)

    return "", codes.CREATED
