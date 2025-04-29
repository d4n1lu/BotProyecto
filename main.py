import random
import string

def gen_pass(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Aquí generamos una contraseña de ejemplo
password = gen_pass(10)
print("Contraseña generada:", password)
