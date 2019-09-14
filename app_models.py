from google.appengine.ext import ndb

class waterfountain(ndb.Model):
    xcoords=ndb.FloatProperty(required=True)
    ycoords= ndb.FloatProperty(required=True)




ANCESTORY_KEY = ndb.Key("waterfountain","waterfountain_root")
