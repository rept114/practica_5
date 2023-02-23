def sumar (lista):
    cont = 0
    x=0
    for i in lista:
        cont += 1
        x = x + i
    return x

 
def multiplicar(lista):
     
    result = 1
    for x in lista:
         result = result * x
    return result

def comparar(lista):
    result = 0
    for i in lista:
        if result > i:
            result = result
        else:
            result = i
    print(result)
    

print(sumar([1, 2, 3, 4, 5]))
print(multiplicar([5, 4, 3, 2, 1, 7]))
comparar([1, 2, 30, 4, 5])
    