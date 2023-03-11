#'w' para escrita, apagando todo o conteudo do arquivo
arquivo=open("arquivo.txt","a")
arquivo.write("palavra\n")
arquivo.close()

#'a' para escrita, adicionar texto ao final do arquivo
arquivo=open("arquivo.txt","a")
arquivo.write("palavra\n")
arquivo.close()

#'r' para leitura
arquivo=open("arquivo.txt","r")
teste=arquivo.read()
arquivo.close()

#'rb' para leitura de arquivos binarios
arquivo=open("arquivo.txt","rb")
teste=arquivo.read()
arquivo.close()

#com o whit não é necessário o comando close
with open("arquivo.txt","a") as ar:
    ar.write("teste\n")
