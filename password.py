from cryptography.fernet import Fernet

def generar_clave():
    return Fernet.generate_key()

def inicializar_cifrador(clave):
    return Fernet(clave)

def cifrar_password(cifrador, password):
    return cifrador.encrypt(password.encode())

def descifrar_password(cifrador, password_cifrado):
    return cifrador.decrypt(password_cifrado).decode()

def guardar_password_en_archivo(filename, password_cifrada):
    with open(filename, 'wb') as file:
        file.write(password_cifrada)


def cargar_password_desde_archivo(filename):
    with open(filename, 'rb') as file:
        return file.read()

if __name__ == "__main__":
    clave = generar_clave()
    cifrador = inicializar_cifrador(clave)

    password_original = "mi_contrasena_secreta"
    password_cifrada = cifrar_password(cifrador, password_original)
    guardar_password_en_archivo("contrasena.dat", password_cifrada)

    password_cifrada_cargada = cargar_password_desde_archivo("contrasena.dat")
    password_descifrada = descifrar_password(cifrador, password_cifrada_cargada)
    print("Contraseña descifrada:", password_descifrada)
