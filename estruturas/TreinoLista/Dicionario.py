dicionario={"a":1,"b":2,"c":3}

print("Sem nada")
for i in dicionario:
    print(i)

print(".values()")
for i in dicionario.values():
    print(i)

print(".items()")
for i,j in dicionario.items():
    print(f"{i}:{j}")
