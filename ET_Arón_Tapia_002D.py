
productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
    '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
    'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
    'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
    'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
    '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
    '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
    'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
    }
stock = {'8475HD': [387990,10],
    '2175HD': [327990,4],
    'JjfFHD': [424990,1],
    'fgdxFHD': [664990,21],
    '123FHD': [290890,32],
    '342FHD': [444990,7],
    'GF75HD': [749990,2],
    'UWU131HD': [349990,1],
    'FS1230HD': [249990,0],
    }

def stock_marca(marca):
    while True:
        if marca == productos["123FHD"][1]:
            print(f"El stock es {stock['123FHD'][1]}")
            return None
        elif marca == productos['2175HD'][1]:
            print(f"El stock es {stock["2175HD"][1]}")
            return None
        elif marca == productos ['342FHD'][1]:
            print(f"El stock es {stock["342FHD"][1]}")
            return None
        elif marca == productos ["8475HD"][1]:
            print(f"El stock es {stock["8475HD"][1]}")
            return None
        elif marca == productos ["fgdxFHD"][1]:
            print(f"El stock es {stock["fgdxFHD"][1]}")
            return None
        elif marca == productos ["FS1230HD"][1]:
            print(f"El stock es {stock["FS1230HD"][1]}")
            return None
        elif marca == productos ["GF75HD"][1]:
            print(f"El stock es {stock["GF75HD"][1]}")
            return None
        elif marca == productos ["JjfFHD"][1]:
            print(f"El stock es {stock["JjfFHD"][1]}")
            return None
        elif marca == productos ["UWU131HD"][1]:
            print(f"El stock es {stock["UWU131HD"][1]}")
            return None
        else:
            print("El stock es 0")
            
while True:
    print("*** MENU PRINCIPAL ***")
    print("1. Stock marca.")
    print("2. Búsqueda por precio.")
    print("3. Actualizar precio.")
    print("4. Salir.")

    opcion=input("Ingrese opción")

    match opcion:
        case "1":
            print(stock_marca)
        case "2":
            precio_minimo=int(input("Ingrese el precio minimo "))
            precio_maximo=int(input("Ingrese el precio maximo "))
        case "3":
            modelo=input("Ingrese modelo a actualizar")
            NEW_price=int(input("Ingrese precio nuevo"))
        case "4":
            print("Programa finalizado.")
            break
        case "_":
            print("Debe seleccionar una opcion valida!!")