#precisa ser instalado
#pip install pyperclip
import pyperclip

#retorna o que estiver na área de transferencia
a=pyperclip.paste()
print(a)

#atribui algo a área de transferencia
pyperclip.copy('ctrl + c')
print(pyperclip.paste())

#esvazia área de transferencia
pyperclip.copy('')
print(pyperclip.paste())
