#Algoritmo de Euclides

def euclides_mdc(dividendo, divisor):
    while divisor != 0:
        temp = divisor
        divisor = dividendo % divisor
        dividendo = temp    
    return dividendo
     
def euclides_recursivo_mdc(dividendo, divisor):
    if divisor == 0:
        return dividendo
    else:
        return euclides_recursivo_mdc(divisor, dividendo % divisor)

euclides_mdc(128, 42)
euclides_recursivo_mdc(125, 37)