import webapp2
import os
import random
import jinja2
# import requests
# from database import defaultdatas
from app_models import waterfountain, ANCESTORY_KEY, bathroom, ANCESTORY_KEYB


the_jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
extensions=['jinja2.ext.autoescape'],autoescape=True)

#????? #GetImages
def GetImages():
    return waterfountain.query().fetch() + bathroom.query().fetch()
def GetWater():
    return waterfountain.query().fetch()
def GetBath():
    return bathroom.query().fetch()
#?????
#make cache
class water(webapp2.RequestHandler):
     def get(self):

         homepage = the_jinja_env.get_template('/templates/home.html')
         print "water: "
         print GetWater()
         self.response.write(homepage.render({"locations": GetWater()}))

class bath(webapp2.RequestHandler):
     def get(self):

         homepage = the_jinja_env.get_template('/templates/home.html')
         print "bath: " 
         print GetBath()
         self.response.write(homepage.render({"locations":GetBath()}))


# {"images":GetImages()}
# class loadImages(webapp2.RequestHandler):
#     def get(self):
#         defaultdatas()
#
class LoginPage(webapp2.RequestHandler):
     def get(self):
         homepage = the_jinja_env.get_template('/templates/login.html')
         self.response.write(homepage.render())
         print('get request completed')
#
#     def post(self):
#         print('starting authentication')
#         try:
#             # retreve token
#             token = self.request.get("id_token")
#             from google.oauth2 import id_token          # BROKEN
#             from google.auth.transport import requests  # BROKEN
#             # Specify the CLIENT_ID of the app that accesses the backend:
#             idinfo = id_token.verify_oauth2_token(token, requests.Request(), CLIENT_ID)
#
#             # Or, if multiple clients access the backend server:
#             # idinfo = id_token.verify_oauth2_token(token, requests.Request())
#             # if idinfo['aud'] not in [CLIENT_ID_1, CLIENT_ID_2, CLIENT_ID_3]:
#             #     raise ValueError('Could not verify audience.')
#
#             if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
#                 raise ValueError('Wrong issuer.')
#
#             # If auth request is from a G Suite domain:
#             # if idinfo['hd'] != GSUITE_DOMAIN_NAME:
#             #     raise ValueError('Wrong hosted domain.')
#
#             # ID token is valid. Get the user's Google Account ID from the decoded token.
#             # next step send to google database
#             userid = idinfo['sub']
#             print(userid)
#         except ValueError:
#
#             # Invalid token
#             print('login: not working')
#             pass

class UploadLocation(webapp2.RequestHandler):
    def get(self):
        homepage = the_jinja_env.get_template('/templates/addImage.html')
        self.response.write(homepage.render())

    def post(self):
        type = int(self.request.get('Type'))
        x = float(self.request.get('x'))
        y= float(self.request.get('y'))

        print x, y, type
        if type == 0:
            bathroom(parent=ANCESTORY_KEYB, xcoords=x, ycoords=y).put()
        else:
            waterfountain(parent=ANCESTORY_KEY, xcoords=x, ycoords=y).put()

        homepage = the_jinja_env.get_template('/templates/addImage.html')
        print(GetImages()  + bathroom.query().fetch())
        self.response.write(homepage.render({"images":GetImages()}))

class Contact(webapp2.RequestHandler):
    def get(self):
        t = the_jinja_env.get_template('templates/contact.html')
        self.response.write(t.render())

app = webapp2.WSGIApplication([
('/',water),
('/bathroom', bath),
('/upload',UploadLocation),
# ('/load', loadImages),
('/contact',Contact)
 ,
 ('/login',LoginPage)
], debug=True)
