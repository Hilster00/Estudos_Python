import zipfile
import pyzipper
import argparse

def zipar_arquivo(arquivo_a_zipar, senha=None):
    # Nome do arquivo zip
    nome_arquivo_zip = f"{arquivo_a_zipar}.zip"

    try:
        # Cria um arquivo zip
        with pyzipper.AESZipFile(nome_arquivo_zip, 'w', compression=pyzipper.ZIP_DEFLATED) as zipf:
            # Adiciona o arquivo ao zip
            zipf.write(arquivo_a_zipar)

            # Define uma senha, se fornecida
            if senha:
                zipf.setpassword(senha)
        
        print(f"Arquivo '{arquivo_a_zipar}' foi zipado para '{nome_arquivo_zip}' com sucesso.")
    
    except Exception as e:
        print(f"Erro ao zipar o arquivo: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Zipar um arquivo com opção de senha.")
    parser.add_argument("arquivo", help="Caminho do arquivo que você deseja zipar")
    parser.add_argument("--senha", help="Senha opcional para proteger o arquivo zipado")

    args = parser.parse_args()

    arquivo_a_zipar = args.arquivo
    senha = args.senha

    zipar_arquivo(arquivo_a_zipar, senha)
