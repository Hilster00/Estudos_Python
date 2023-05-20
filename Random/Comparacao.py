import secrets
import random

# Gerando uma lista de números aleatórios entre 0 e 9 (usando secrets)
random_numbers_secrets = [secrets.randbelow(10) for _ in range(5)]
print("Números aleatórios (secrets):", random_numbers_secrets)

# Gerando uma lista de números aleatórios entre 0 e 9 (usando random)
random_numbers_random = [random.randint(0, 9) for _ in range(5)]
print("Números aleatórios (random):", random_numbers_random)

# Gerando um token URL seguro com 16 caracteres (usando secrets)
secure_token_url = secrets.token_urlsafe(16)
print("Token URL seguro (secrets):", secure_token_url)

# Embaralhando os elementos de uma lista (usando secrets)
my_list = [1, 2, 3, 4, 5]
secrets.shuffle(my_list)
print("Lista embaralhada (secrets):", my_list)

# Gerando um número criptograficamente seguro entre 1 e 100 (usando secrets)
secure_random_number = secrets.randbits(7) + 1
print("Número criptograficamente seguro:", secure_random_number)
