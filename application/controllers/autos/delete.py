import config
import hashlib
import app

class Delete:
    
    def __init__(self):
        pass

    def GET(self, id_auto, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_DELETE(id_auto) # call GET_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/logout') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_auto, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege
            if session_privilege == 0: # admin user
                return self.POST_DELETE(id_auto) # call POST_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/logout') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html
   
    @staticmethod
    def GET_DELETE(id_auto, **k):
        message = None # Error message
        id_auto = config.check_secure_val(str(id_auto)) # HMAC id_auto validate
        result = config.model.get_autos(int(id_auto)) # search  id_auto
        result.id_auto = config.make_secure_val(str(result.id_auto)) # apply HMAC for id_auto
        return config.render.delete(result, message) # render delete.html with user data
    
    @staticmethod
    def POST_DELETE(id_auto, **k):
        form = config.web.input() # get form data
        form['id_auto'] = config.check_secure_val(str(form['id_auto'])) # HMAC id_auto validate
        result = config.model.delete_autos(form['id_auto']) # get autos data
        if result is None: # delete error
            message = "El registro no se puede borrar" # Error messate
            id_auto = config.check_secure_val(str(id_auto))  # HMAC user validate
            id_auto = config.check_secure_val(str(id_auto))  # HMAC user validate
            result = config.model.get_autos(int(id_auto)) # get id_auto data
            result.id_auto = config.make_secure_val(str(result.id_auto)) # apply HMAC to id_auto
            return config.render.delete(result, message) # render delete.html again
        else:
            raise config.web.seeother('/autos') # render autos delete.html 
