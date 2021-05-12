import random

def ask_number(text):
    user_input = input(text)
    user_input_check = user_input_type_check(user_input)
        
    # while not user_input_check:
    if user_input_check:
        user_input_as_number = int(user_input)
        return int(user_input_as_number)
    else:
        print('Porfavor ingresa un tipo valido de dato\n')  
        return ask_number(text)  

def user_input_type_check(user_input):
    try: 
        int(user_input)
        return True
    except:
        return False

def generar_contrasena():
    MAYUS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
    MINUS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
    NUMS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    CHARS = ['*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"']

    caracteres = MAYUS + MINUS + NUMS + CHARS

    contrasena = []
    
    pass_lenght = ask_number("Ingresa la longitud de tu contrasena \n--> ")

    for i in range(pass_lenght):
        caracter_random = random.choice(caracteres)
        contrasena.append(caracter_random)

    contrasena = "".join(contrasena)
    return contrasena


def run():
    contrasena = generar_contrasena()
    print('Tu nueva contraseña es: ' + contrasena)


if __name__ == '__main__':
    run()