import os,dotenv

#carrega valiaveis locais
dotenv.load_dotenv()

#lista as variaveis locais
#print(os.environ)

#carrega dados da variavel local
print(os.getenv("USER"))
