#check password strength
def check_password_strength(password):
    if len(password) < 8:
        raise Exception("error: password must be >=8 characters")
    print("password is strong")

try:
    password = input('enter a password = ')
    check_password(password)
except Exception as e:
    print(e)
    