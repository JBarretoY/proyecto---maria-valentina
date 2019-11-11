from tinydb import TinyDB
from tinydb import where

class Movie:
    def __init__(self,title,clasification,gender,rating,director,distribution):
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
    
    def getAllMovies(self):
        table =  self.db.table('movies')
        print(table.all())
        
    def getMovie(self):
        table = self.db.table('movies')
        resp = table.search(where('title') == 'Rey leon')
        print(resp)
        
    def removeMovie(self):
        table = self.db.table('movies')
        resp  = table.remove(where('title') == 'Interstellar') 
        print(resp)
        
    def updateMovie(self):
        table = self.db.table('movies')
        resp = table.update({'title':'Lion King'}, where('title') == 'Rey leon')
        print(resp)
        
    def purgeTable(self):
        self.db.purge_table('movies')

test = Movie('Rey leon', 'A', 'Animacion', 10, "yo mismo", ['a','b','c'])
test.removeMovie()
        