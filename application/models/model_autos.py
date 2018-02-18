import web
import config

db = config.db


def get_all_autos():
    try:
        return db.select('autos')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_autos(id_auto):
    try:
        return db.select('autos', where='id_auto=$id_auto', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None


def delete_autos(id_auto):
    try:
        return db.delete('autos', where='id_auto=$id_auto', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None


def insert_autos(marca,modelo,tipo,inventario,precio):
    try:
        return db.insert('autos',marca=marca,
modelo=modelo,
tipo=tipo,
inventario=inventario,
precio=precio)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None


def edit_autos(id_auto,marca,modelo,tipo,inventario,precio):
    try:
        return db.update('autos',id_auto=id_auto,
marca=marca,
modelo=modelo,
tipo=tipo,
inventario=inventario,
precio=precio,
                  where='id_auto=$id_auto',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None
