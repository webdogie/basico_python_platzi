def run():
    K = 1.609344

    print("Bienvenido a tu calculadora de distancias favorita!\n\n")
    user_input_pick = input("Ingresa lo que quieres convertir: millas | kilometros\n--> ")


    if user_input_pick == "kilometros":
        user_input_quantity = float(input("Ingresa cuantos kilometros quieres convertir a millas\n--> "))
        result = round(user_input_quantity / K, 2)
        print(f"El resultado es {result} mi")

    elif user_input_pick == "millas":
        user_input_quantity = float(input("Ingresa cuantas millas quieres convertir a kilometros\n--> "))
        result = round(user_input_quantity * K, 2)
        print(f"El resultado es {result} Km")
    else:
        print("Ingresa la unidad correcta. 🤔")
        return run()


if __name__ == '__main__':
    while True:
        run()