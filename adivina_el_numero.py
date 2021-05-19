import random
import sanitise_user_input as sanitise

def game_loop(random_num):

    user_input = sanitise.ask_number("Adivina el numero! --> ")

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
        lifes = sanitise.ask_number("Ingresa el numero de intentos quieres tener para adivinar --> ", "Porfavor ingresa un tipo valido de dato\n")
        
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