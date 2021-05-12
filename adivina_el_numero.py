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

def game_loop(random_num):

    user_input = ask_number("Adivina el numero! --> ")

    if random_num == user_input:
        return True

    elif random_num > user_input:
        print("Intenta un numero mas grande! ⬆\n")
        return False

    elif random_num < user_input:
        print("Intenta un numero mas pequeno! ⬇\n")
        return False

def run():
    while True:
        lifes = ask_number("Ingresa el numero de intentos quieres tener para adivinar --> ")
        
        rand_number = random.randint(1, 100)

        while lifes > 0:
            if game_loop(rand_number):
                print("------ YOU WIN ------\n")
                break
            else:                   
                lifes -= 1      
        if lifes <= 0:
            print("------ GAME OVER ------\n")

if __name__ == '__main__':
    run()