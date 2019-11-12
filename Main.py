from Movie import Movie
import sys
from os import system
from time import sleep

class Main: 
    
    def main(self):
        
        try:
            output = int(self.menu())
        
            if output == 0:
                sys.exit()
                
            elif output == 1:
                title  = input("Nombre de la pelicula: ")
                gender = input("Genero: ")
                clasi  = input("Clasificacion: ")
                rating = input("Rating: ")
                
                direc  = input("Director: ")
                distri = input("Reparto (separado por ',')")
                dis = distri.split(',')
                
                movie = Movie(title,clasi,gender,rating,direc,dis)
                resp  = movie.saveMovie()
                
                if resp:
                    print("Pelicula registrada exitosamente")
                    system('clear')
                    self.main()  
                    
            elif output == 2:
                index  = input("indique el criterio de busqueda: ")
                search = input("indique el valor de busqueda: ")
                movie  = Movie()
                resp = movie.getMovie(index, search)
                
                if resp:
                    print("Pelicula encontrada!")
                    print(resp)
                    sleep(4)
                    system('clear')
                    self.main()
                    
                else:
                    print("Pelicula no encontrada")
                    sleep(4)
                    system('clear')
                    self.main()
            elif output == 3:
                index  = input("indique el criterio de busqueda: ")
                search = input("indique el valor de busqueda: ")
                movie  = Movie()
                resp = movie.removeMovie(index, search)
                
                if resp:
                    print("Pelicula Eliminada!")
                    sleep(4)
                    system('clear')
                    self.main()
                    
                else:
                    print("Pelicula no encontrada")
                    sleep(4)
                    system('clear')
                    self.main() 
                    
            elif output == 4:
                index  = input("indique el criterio de busqueda: ")
                search = input("indique el valor a buscar: ")
                field  = input("indique el campo a actualizar: ")
                value  = input("indique el nuevo valor: ")
                
                movie = Movie()
                resp = movie.updateMovie(index, field, value, search)
                
                if resp:
                    print("Pelicula actualizada")
                    sleep(3)
                    system("clear")
                    self.menu()
                else:
                    print("Pelicula no encontrada")
                    sleep(3)
                    system("clear")
                    self.menu()                
            else: 
                print("Opcion invalida!")
                sleep(1)
                system('clear')
                self.main()
        except ValueError:
            print("Error en tipo de dato")
            sleep(2)
            system('clear')
            self.main()            
            
    def menu(self):
    
        print("#### Bienvenido al sistema ####")
        print("1. Agregar pelicula")
        print("2. Buscar Pelicula")
        print("3. Eliminar Pelicula")
        print("4. Actualizar Pelicula")
        print("0. para salir")
        key = input("Introduzca una opcion: ")
        return key
    
def main():
    main = Main()
    main.main()
    
main()