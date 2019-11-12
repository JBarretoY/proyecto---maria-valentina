from tinydb import TinyDB
from tinydb import where

class Movie:
    def __init__(self,title=None,clasification=None,gender=None,rating=None,director=None,distribution=None):
        self.title = title
        self.clasification = clasification
        self.gender = gender
        self.rating = rating
        self.director = director
        self.distribution = distribution
        self.db = TinyDB('./db.json')
    
    def saveMovie(self):
        table = self.db.table('movies')
        table.insert({'title': self.title, 'clasification': self.clasification,'gender': self.gender,
                   'rating':self.rating,'director':self.director,'distribution':self.distribution})
        return True
    
    def getAllMovies(self):
        table =  self.db.table('movies')
        print(table.all())
        
    def getMovie(self,index,value):
        if(self.searchMovie(index, value) > 0):
            table = self.db.table('movies')
            resp = table.search(where(index) == value)
            return resp
        else:
            return False
        
    def removeMovie(self,index,value):
        if(self.searchMovie(index, value) > 0):
            table = self.db.table('movies')
            table.remove(where(index) == value) 
            return True
        else:
            return False
        
    def updateMovie(self,index,field,value,search):
        if(self.searchMovie(index, search)):
            table = self.db.table('movies')
            table.update({field:value}, where(index) == search)
            return True     
        else:
            return False
        
    def purgeTable(self):
        self.db.purge_table('movies')
        
    def searchMovie(self,index,value):
        table = self.db.table('movies')
        return len(table.search(where(index) == value))
        