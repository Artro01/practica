import config
import hashlib
import app

class Delete:
    
    def __init__(self):
        pass
    def GET(self, id_equipo, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_DELETE(id_equipo) # call GET_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/logout') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_equipo, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege
            if session_privilege == 0: # admin user
                return self.POST_DELETE(id_equipo) # call POST_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/logout') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html


    @staticmethod
    def GET_DELETE(id_equipo, **k):
        message = None # Error message
        id_equipo = config.check_secure_val(str(id_equipo)) # HMAC id_equipo validate
        result = config.model.get_equipos(int(id_equipo)) # search  id_equipo
        result.id_equipo = config.make_secure_val(str(result.id_equipo)) # apply HMAC for id_equipo
        return config.render.delete(result, message) # render delete.html with user data
    @staticmethod
    def POST_DELETE(id_equipo, **k):
        form = config.web.input() # get form data
        form['id_equipo'] = config.check_secure_val(str(form['id_equipo'])) # HMAC id_equipo validate
        result = config.model.delete_equipos(form['id_equipo']) # get equipos data
        if result is None: # delete error
            message = "El registro no se puede borrar" # Error messate
            id_equipo = config.check_secure_val(str(id_equipo))  # HMAC user validate
            id_equipo = config.check_secure_val(str(id_equipo))  # HMAC user validate
            result = config.model.get_equipos(int(id_equipo)) # get id_equipo data
            result.id_equipo = config.make_secure_val(str(result.id_equipo)) # apply HMAC to id_equipo
            return config.render.delete(result, message) # render delete.html again
        else:
            raise config.web.seeother('/equipos') # render equipos delete.html 
