from cryptography.fernet import Fernet

def autenticar_usuario(usuario, contrasena):
    """Autentica a un usuario con su contraseña."""
    usuarios_validos = {
        "admin": "1234",
        "user1": "password1",
        "user2": "password2"
    }
    return usuarios_validos.get(usuario) == contrasena

def generar_clave():
    """Genera una clave para encriptación."""
    return Fernet.generate_key()

def encriptar_datos(datos, clave):
    """Encripta datos usando una clave dada."""
    fernet = Fernet(clave)
    return fernet.encrypt(datos.encode())

def desencriptar_datos(datos_encriptados, clave):
    """Desencripta datos encriptados usando una clave dada."""
    fernet = Fernet(clave)
    return fernet.decrypt(datos_encriptados).decode()

def validar_usuario(usuario):
    """Valida si un usuario es válido."""
    return usuario in ["admin", "user1", "user2"]

def cambiar_contrasena(usuario, nueva_contrasena):
    """Cambia la contraseña de un usuario."""
    # Lógica para cambiar la contraseña
    pass 