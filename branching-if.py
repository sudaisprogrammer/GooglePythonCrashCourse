

def check_username_length(username):
    if len(username)>3 and len(username)<10:
        print("valid username")
    else:
        print("invalid username")

check_username_length("Maria")
check_username_length("mia")
check_username_length("kayley")
        