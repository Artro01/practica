import web
import config

db = config.db


def get_all_equipos():
    try:
        return db.select('equipos')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_equipos(id_equipo):
    try:
        return db.select('equipos', where='id_equipo=$id_equipo', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None


def delete_equipos(id_equipo):
    try:
        return db.delete('equipos', where='id_equipo=$id_equipo', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None


def insert_equipos(marca,modelo,tipo,inventario,precio):
    try:
        return db.insert('equipos',marca=marca,
modelo=modelo,
tipo=tipo,
inventario=inventario,
precio=precio)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None


def edit_equipos(id_equipo,marca,modelo,tipo,inventario,precio):
    try:
        return db.update('equipos',id_equipo=id_equipo,
marca=marca,
modelo=modelo,
tipo=tipo,
inventario=inventario,
precio=precio,
                  where='id_equipo=$id_equipo',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None
