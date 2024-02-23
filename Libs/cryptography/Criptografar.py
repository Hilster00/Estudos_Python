from cryptography.fernet import Fernet

def gerar_chave():
    return Fernet.generate_key()

def criptografar_string(chave, texto):
    fernet = Fernet(chave)
    texto_bytes = texto.encode()
    texto_criptografado = fernet.encrypt(texto_bytes)
    return texto_criptografado

def descriptografar_string(chave, texto_criptografado):
    fernet = Fernet(chave)
    texto_descriptografado_bytes = fernet.decrypt(texto_criptografado)
    texto_descriptografado = texto_descriptografado_bytes.decode()
    return texto_descriptografado

# Gerar uma chave de criptografia
chave = gerar_chave()

# String a ser criptografada
texto_original = "Esta é uma string que será criptografada."

# Criptografar a string
texto_criptografado = criptografar_string(chave, texto_original)
print("Texto criptografado:", texto_criptografado)

# Descriptografar a string
texto_descriptografado = descriptografar_string(chave, texto_criptografado)
print("Texto descriptografado:", texto_descriptografado)
