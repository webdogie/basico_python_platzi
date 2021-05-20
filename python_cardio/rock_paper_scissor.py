def run():
  print("Bienvenido al juego piedra, papel o tijera!\n\nIngresa lo siguiente: piedra | papel | tijera\n")
  player1 = input("Jugador 1 ingresa tu eleecion\n--> ")
  player2 = input("Jugador 2 ingresa tu eleecion\n--> ")

  rock = "piedra"
  paper = "papel"
  scissor = "tijera"

  if player1 == player2:
      print("----------------\n-----EMPATE-----\n----------------\n")
  elif (player1 == rock and player2 == scissor) or (player1 == paper and player2 == rock) or (player1 == scissor and player2 == paper):
      print("------------------------\n-----Jugador 1 Gana!----\n------------------------\n")
                                     
  else:
      print("------------------------\n-----Jugador 2 Gana!----\n------------------------\n")


if __name__ == '__main__':
    while True:
        run()