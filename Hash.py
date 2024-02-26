import hashlib

def calcular_hash(texto):
    # Crie um objeto de hash usando o algoritmo SHA-256
    hasher = hashlib.sha256()
    
    # Atualize o objeto de hash com o texto fornecido
    hasher.update(texto.encode('utf-8'))
    
    # Obtenha o hash calculado em hexadecimal
    return hasher.hexdigest()

# Exemplo de uso
texto = "Este é um texto de exemplo para calcular o hash."
hash_calculado = calcular_hash(texto)
print("Texto original:", texto)
print("Hash SHA-256:", hash_calculado)
