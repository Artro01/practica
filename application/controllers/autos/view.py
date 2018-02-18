import config
import hashlib
import app


class View:

    def __init__(self):
        pass

    def GET(self, id_auto):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_VIEW(id_auto) # call GET_VIEW() function
            elif session_privilege == 1: # guess user
                return self.GET_VIEW(id_auto) # call GET_VIEW() function
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_VIEW(id_auto):
        id_auto = config.check_secure_val(str(id_auto)) # HMAC id_auto validate
        result = config.model.get_autos(id_auto) # search for the id_auto data
        return config.render.view(result) # render view.html with id_auto data
