import math

def calc_vol(area, height):
    volume = round(area * height)
    return volume

def run():
    print("Bienvenido a tu calculadora de volumenes favorita!\n\ntrabajaremos con centimetros\n\n")
    user_input_pick = input("Ingresa la figura a la que quieres conocer su volumen: cilindro | cono | piramide|\n--> ")


    if user_input_pick == "cilindro":
        radius = float(input("Ingresa el radio del cilindro\n--> "))
        height = float(input("Ingresa la altura del cilindro\n--> "))

        volume = calc_vol((radius**2) * math.pi, height)

        print(f"El volumen es: {volume}cm")

    elif user_input_pick == "cono":
        height = float(input("Ingresa la altura del cono\n--> "))
        radius = float(input("Ingresa el radio de la base del cono\n--> "))

        volume = calc_vol((radius**2) * math.pi, height) / 3

        print(f"El volumen es: {volume}cm")

    elif user_input_pick == "piramide":
        height = float(input("Ingresa la altura de la piramide\n--> "))
        area = float(input("Ingresa el area de la base de tu piramide\n--> "))

        volume = calc_vol(area, height) / 3
        print(f"El volumen es: {volume}cm")
    else:
        print("Ingresa una figura correctamente. 🤔")
        return run()


if __name__ == '__main__':
    while True:
        run()