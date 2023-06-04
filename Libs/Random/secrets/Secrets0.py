import secrets

# Gerando número aleatório entre 0 e 100 (não inclusivo)
print("Exemplo 1 - Gerando número aleatório entre 0 e 100: ")
print(secrets.randbelow(100))
print()

# Escolhendo um elemento aleatório de uma lista
print("Exemplo 2 - Escolhendo um elemento aleatório de uma lista: ")
lista = ["azul", "verde", "amarelo", "vermelho", "roxo"]
print(secrets.choice(lista))
print()

# Gerando token de segurança aleatório com 16 bytes
print("Exemplo 3 - Gerando token de segurança aleatório com 16 bytes: ")
token = secrets.token_bytes(16)
print(token)
print()

# Gerando token de segurança aleatório em formato hexadecimal com 16 bytes
print("Exemplo 4 - Gerando token de segurança aleatório em formato hexadecimal com 16 bytes: ")
token_hex = secrets.token_hex(16)
print(token_hex)
print()

# Gerando token de segurança aleatório em formato url-safe com 16 bytes
print("Exemplo 5 - Gerando token de segurança aleatório em formato url-safe com 16 bytes: ")
token_urlsafe = secrets.token_urlsafe(16)
print(token_urlsafe)
