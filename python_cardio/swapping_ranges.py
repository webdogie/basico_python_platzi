
def compare():
	if user_input_limit_compare < user_input_limit_lower:
		print(f"El numero {user_input_limit_compare} es menor al limite inferrio {user_input_limit_lower}\n")

	elif user_input_limit_compare > user_input_limit_upper:
		print(f"El numero {user_input_limit_compare} es mayor al limite seuperior {user_input_limit_upper}\n")
	else:
		print(f"El numero {user_input_limit_compare} esta entre {user_input_limit_lower} y {user_input_limit_upper}\n")

if __name__ == '__main__':
	user_input_limit_lower = float(input("Ingresa el limite inferior\n--> "))
	user_input_limit_upper = float(input("Ingresa el limite superior\n--> "))

	while True:
		user_input_limit_compare = float(input("Ingresa el numero cual quieres saber su ubicacion\n--> "))
		compare()