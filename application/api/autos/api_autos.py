import web
import config
import json


class Api_autos:
    def get(self, id_auto):
        try:
            # http://0.0.0.0:8080/api_autos?user_hash=12345&action=get
            if id_auto is None:
                result = config.model.get_all_autos()
                autos_json = []
                for row in result:
                    tmp = dict(row)
                    autos_json.append(tmp)
                web.header('Content-Type', 'application/json')
                return json.dumps(autos_json)
            else:
                # http://0.0.0.0:8080/api_autos?user_hash=12345&action=get&id_auto=1
                result = config.model.get_autos(int(id_auto))
                autos_json = []
                autos_json.append(dict(result))
                web.header('Content-Type', 'application/json')
                return json.dumps(autos_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            autos_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(autos_json)

# http://0.0.0.0:8080/api_autos?user_hash=12345&action=put&id_auto=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=0
    def put(self, marca,modelo,tipo,inventario,precio):
        try:
            config.model.insert_autos(marca,modelo,tipo,inventario,precio)
            autos_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(autos_json)
        except Exception as e:
            print "PUT Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_autos?user_hash=12345&action=delete&id_auto=1
    def delete(self, id_auto):
        try:
            config.model.delete_autos(id_auto)
            autos_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(autos_json)
        except Exception as e:
            print "DELETE Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_autos?user_hash=12345&action=update&id_auto=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=default.jpg
    def update(self, id_auto, marca,modelo,tipo,inventario,precio):
        try:
            config.model.edit_autos(id_auto,marca,modelo,tipo,inventario,precio)
            autos_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(autos_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            autos_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(autos_json)

    def GET(self):
        user_data = web.input(
            user_hash=None,
            action=None,
            id_auto=None,
            marca=None,
            modelo=None,
            tipo=None,
            inventario=None,
            precio=None,
        )
        try:
            user_hash = user_data.user_hash  # user validation
            action = user_data.action  # action GET, PUT, DELETE, UPDATE
            id_auto=user_data.id_auto
            marca=user_data.marca
            modelo=user_data.modelo
            tipo=user_data.tipo
            inventario=user_data.inventario
            precio=user_data.precio
            # user_hash
            if user_hash == '12345':
                if action is None:
                    raise web.seeother('/404')
                elif action == 'get':
                    return self.get(id_auto)
                elif action == 'put':
                    return self.put(marca,modelo,tipo,inventario,precio)
                elif action == 'delete':
                    return self.delete(id_auto)
                elif action == 'update':
                    return self.update(id_auto, marca,modelo,tipo,inventario,precio)
            else:
                raise web.seeother('/404')
        except Exception as e:
            print "WEBSERVICE Error {}".format(e.args)
            raise web.seeother('/404')
