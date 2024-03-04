import json
from socialmedia import *

def leer_json():
    with open('socialmedia2.json', 'r', encoding='utf-8') as archivo:
        data = json.load(archivo)
    return data
    
def funcion(posts):
    opcion = 0
    # Menú de opciones
    while opcion != '6':
        print("\nMenú:")
        print("1. Mostrar total de likes por usuario")
        print("2. Mostrar total de comentarios en todos los posts")
        print("3. Buscar publicaciones de un usuario")
        print("4. Mostrar comentarios de un usuario en publicaciones con más de 100 likes")
        print("5. Mostrar usuarios que han compartido más de X veces")
        print("6. Salir")
        
        opcion = input("Seleccione una opción (1-6): ")
        
        if opcion == '1':
            opcion1(posts)
        elif opcion == '2':
            opcion2(posts)
        elif opcion == '3':
            username = input("Ingrese el nombre de usuario: ")
            opcion3(posts, username)
        elif opcion == '4':
            username = input("Ingrese el nombre de usuario: ")
            opcion4(posts, username)
        elif opcion == '5':
            min_comparticiones = int(input("Ingrese el número mínimo de comparticiones: "))
            opcion5(posts, min_comparticiones)
        elif opcion == '6':
            print("El programa ha finalizado")
        else:
            print("Introduce un numero del 1-6")

posts = leer_json()
funcion(posts)
