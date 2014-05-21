from pymongo import MongoClient
from time import strftime

class DBlayer(object):

    def __init__(self,uri='mongodb://localhost:27017/',db='beatdb',DEBUG=False):

        self.DEBUG = DEBUG

        if self.DEBUG:
            print "Starting DBlayer() INIT ..."

        self.dbclient = MongoClient(uri)
        self.db = self.dbclient[db]
        
        self.users = self.db['users']
        self.posts = self.db['posts']
        self.categories = self.db['categories']
        self.settings = self.db['settings']

        if self.DEBUG:
            print "DBlayer() INIT completed successfully."
            
    #
    #Crud(posts,users,categories,settings)
    #
    
    def addUser(self, new, user): #user is the person(id) doing this activity
        """
        
        user = {
            'ident' : '1d2fb3a4',
            'username' : 'mattttt',
            'password' : 'letmein',
            'qty' : '15',
            'last' : '234562035',
            'added' : '123455349',
            'admin' : 'false'
        }
        
        """
        ##make sure ident is only visible to the owner
        
        print self.users.find_one({'ident' : user})['admin']
        
    def getUser(self, user):###user is 'username' in this instance
        result = self.users.find_one({'username':user})
        return result
        
    def getAllUsers(self, admin=False):
        results = self.users.find({'admin':admin})
        return results
        
    def modUser(self, new, user):
        print 'didnt do anything'
        return False
        
    def delUser(self, user):
        print 'didnt do anything'
        return False
        

