import config
import hashlib
import app

class Edit:
    
    def __init__(self):
        pass

    def GET(self, id_equipo, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_EDIT(id_equipo) # call GET_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/logout') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_equipo, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.POST_EDIT(id_equipo) # call POST_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/logout') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html


    @staticmethod
    def GET_EDIT(id_equipo, **k):
        message = None # Error message
        id_equipo = config.check_secure_val(str(id_equipo)) # HMAC id_equipo validate
        result = config.model.get_equipos(int(id_equipo)) # search for the id_equipo
        result.id_equipo = config.make_secure_val(str(result.id_equipo)) # apply HMAC for id_equipo
        return config.render.edit(result, message) # render equipos edit.html

    @staticmethod
    def POST_EDIT(id_equipo, **k):
        form = config.web.input()  # get form data
        form['id_equipo'] = config.check_secure_val(str(form['id_equipo'])) # HMAC id_equipo validate
        # edit user with new data
        result = config.model.edit_equipos(
            form['id_equipo'],form['marca'],form['modelo'],form['tipo'],form['inventario'],form['precio'],
        )
        if result == None: # Error on udpate data
            id_equipo = config.check_secure_val(str(id_equipo)) # validate HMAC id_equipo
            result = config.model.get_equipos(int(id_equipo)) # search for id_equipo data
            result.id_equipo = config.make_secure_val(str(result.id_equipo)) # apply HMAC to id_equipo
            message = "Error al editar el registro" # Error message
            return config.render.edit(result, message) # render edit.html again
        else: # update user data succefully
            raise config.web.seeother('/equipos') # render equipos index.html
