availableMovies = ["matrix", "prisioners", "el camino", "hereditary", "midsommar"]
n= 1
ticket = 35
reserves = {}
name = input("Ingrese su nombre: " )
print(f"Estas son las peliculas disponibles:" )
for i in availableMovies:
    print(f"{n}. {i}")
    n += 1
movie = input("Ingrese la pelicula que desea ver: ")

if movie in availableMovies:
    howMany = int(input(f"Vas a ver: {movie}" f"\nPrecio por entrada: {ticket}" f"\nCuantos tickets quieres comprar? "))
    price = ticket * howMany
    print(f"----- Resumen de compra ------"f"\nTu nombre: {name}" f"\nVas a ver: {movie}" "\n----Pago total ----", f"\nQ{price}")
    reserves[name] = movie

else: print("Titulo incorrecto, prueba de nuevo amigo")

def change_price(newPrice):
    ticket = int(input("Ingrese un nuevo precio para la entrada: "))

####Para imprimir las reservas en diccionario ---->
# print(f"Las reservas son: {reserves}")
