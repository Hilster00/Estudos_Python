lista=[1,2,3,4,5,6,7,8,9,0]

l1=[i for i in lista]
l2=[i*3 for i in lista]
l3=[[i,j] for i in lista for j in range(2)]

print(lista)
print(l1)
print(l2)
print(l3)   
    
