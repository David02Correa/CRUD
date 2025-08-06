PASSWORD = 'platzi'

def password_required(func):
    def wrapper(*args, **kwargs):
        password = input('Ingrese la contraseña: ')
        if password == PASSWORD:
            return func(*args, **kwargs)
        else:
            print('Contraseña incorrecta')
    return wrapper
@password_required

def needs_password():
    print('la contraseña es correcta')


def say_my_name(name):
    print(f'Hola {name}')
if __name__ == "__main__":
    needs_password()