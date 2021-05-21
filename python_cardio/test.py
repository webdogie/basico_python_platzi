def run():
    print("Bienvenido al juego piedra, papel o tijera!\n\nIngresa lo siguiente: piedra | papel | tijera\n")

    game_state = [0, 0]

    rock = "piedra"
    paper = "papel"
    scissor = "tijera"

    while game_state[0] < 3 or game_state[1] < 3:
        player1 = input("Jugador 1 ingresa tu eleecion\n--> ")
        player2 = input("Jugador 2 ingresa tu eleecion\n--> ")
        
        if (player1 == rock and player2 == scissor) or (player1 == paper and player2 == rock) or (player1 == scissor and player2 == paper):

            if game_state[0] >= 3:
                print("------------------------\n-----Jugador 1 Gana!----\n------------------------\n")
                return

            game_state[0] += 1
            print (f"El jugador n1 gano 1 punto")
            print (f"El jugador n1 tiene {game_state[0]} puntos")

        elif player1 == player2:
            print("----------------\n-----EMPATE-----\n----------------\n")                            
            print("----------\nNingun jugador obtiene punto\n----------\n")                            
        else:
            if game_state[1] >= 3:
                print("------------------------\n-----Jugador 2 Gana!----\n------------------------\n")
                return

            game_state[1] += 1
            print (f"El jugador n2 gano 1 punto")
            print (f"El jugador n2 tiene {game_state[1]} puntos")


if __name__ == '__main__':
    run()