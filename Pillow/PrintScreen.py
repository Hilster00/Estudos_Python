from PIL import ImageGrab

# Capturar a tela
imagem = ImageGrab.grab()

# Salvar a imagem
imagem.save("tela.png")

# Imprimir a imagem em uma impressora
imagem.print()
