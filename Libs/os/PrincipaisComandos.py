import os

# Obtendo o diretório atual
current_dir = os.getcwd()
print("Diretório atual:", current_dir)

# Listando o conteúdo de um diretório
dir_contents = os.listdir(current_dir)
print("Conteúdo do diretório:")
for item in dir_contents:
    print(item)

# Criando um novo diretório
new_dir = "novo_diretorio"
os.mkdir(new_dir)
print("Novo diretório criado:", new_dir)

# Renomeando um arquivo ou diretório
old_name = "arquivo_antigo.txt"
new_name = "arquivo_novo.txt"
os.rename(old_name, new_name)
print("Arquivo/diretório renomeado:", new_name)

# Verificando se um arquivo ou diretório existe
file_path = "meu_arquivo.txt"
exists = os.path.exists(file_path)
print("Arquivo existe:", exists)

# Removendo um arquivo
os.remove(file_path)
print("Arquivo removido:", file_path)

# Removendo um diretório
os.rmdir(new_dir)
print("Diretório removido:", new_dir)
