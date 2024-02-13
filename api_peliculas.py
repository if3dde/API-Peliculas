import requests

api_key = "4aec388d0829e9d2cecf914b91957ed0"

nombre_pelicula = input("Ingrese el nombre de la película: ")

url = f"https://api.themoviedb.org/3/search/movie?query={nombre_pelicula}&language=es-ES&api_key={api_key}"

respuesta = requests.get(url)

datos = respuesta.json()

try:
    print("--------------------------------------------------")
    print(datos["results"][0]["title"])
    print("")
    print("Fecha de lanzamiento: " + datos["results"][0]["release_date"])
    print("")
    print(datos["results"][0]["overview"])
    print("")
    print("--------------------------------------------------")

except:
    print("Pelicula no encontrada")
    print("")