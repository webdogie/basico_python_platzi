def user_input_type_check(user_input, expected):
    if type(user_input) == expected:
        return True
    else:
        return False


# Verifies if it is a number, else return same question
def ask_number(text, error_output, expected):
    user_input = input(text)
    user_input_check = user_input_type_check(user_input, expected)
        
    if user_input_check:
        return expected(user_input)
    else:
        print(error_output)  
        return ask_number(text, error_output, expected)  