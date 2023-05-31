from pathlib import Path
from PIL import Image

ROOT_FOLDER = Path(__file__).parent

nome=input("Nome da imagem:")
imagem = ROOT_FOLDER /nome


novo_nome=input("Nome da nova imagem:")
nova_imagem = ROOT_FOLDER /novo_nome

pil_image = Image.open(imagem)
largura, altura = pil_image.size

nova_altura = int(input("Altura:"))
nova_largura = round(largura * nova_altura/altura)

new_image = pil_image.resize(size=(nova_largura, nova_largura))
new_image.save(
    nova_imagem,
    optimize=True,
    quality=90,
)
