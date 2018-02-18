import config
import hashlib
import app

class Edit:
    
    def __init__(self):
        pass

    def GET(self, id_auto, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_EDIT(id_auto) # call GET_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/logout') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_auto, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.POST_EDIT(id_auto) # call POST_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/logout') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_EDIT(id_auto, **k):
        message = None # Error message
        id_auto = config.check_secure_val(str(id_auto)) # HMAC id_auto validate
        result = config.model.get_autos(int(id_auto)) # search for the id_auto
        result.id_auto = config.make_secure_val(str(result.id_auto)) # apply HMAC for id_auto
        return config.render.edit(result, message) # render autos edit.html

    @staticmethod
    def POST_EDIT(id_auto, **k):
        form = config.web.input()  # get form data
        form['id_auto'] = config.check_secure_val(str(form['id_auto'])) # HMAC id_auto validate
        # edit user with new data
        result = config.model.edit_autos(
            form['id_auto'],form['marca'],form['modelo'],form['tipo'],form['inventario'],form['precio'],
        )
        if result == None: # Error on udpate data
            id_auto = config.check_secure_val(str(id_auto)) # validate HMAC id_auto
            result = config.model.get_autos(int(id_auto)) # search for id_auto data
            result.id_auto = config.make_secure_val(str(result.id_auto)) # apply HMAC to id_auto
            message = "Error al editar el registro" # Error message
            return config.render.edit(result, message) # render edit.html again
        else: # update user data succefully
            raise config.web.seeother('/autos') # render autos index.html
