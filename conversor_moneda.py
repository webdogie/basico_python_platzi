# while True:
#     try:
#       money = float(input("Cantidad de pesos a convertir en dolares: "))
#       dollar_value = 700
#       to_dollar = money / dollar_value
#       print("$" + str(round(to_dollar,2)))
#     except:
#       print("No se entrego un numero 🤨\nIntenta de nuevo abajo ↓↓↓\n")

while True:
    try:
      money = float(input("Cantidad de dolares a convertir en pesos: "))
      peso_value = 0.0014
      to_peso = money / peso_value
      print("$" + str(round(to_peso, 2)))
    except:
      print("No se entrego un numero 🤨\nIntenta de nuevo abajo ↓↓↓\n")