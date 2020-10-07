#Exercicio 3 - script_hipotenusa.py

#Para essa atividade tive de desenvolver um código que calculasse o número inteiro correspondente ao quadrado da hipotenusa
#Para isso optei pelo uso de um loop while para otimizar o código, mas apesar disso foi utilizado a função isintance() e as condicionais (if, else) como foi ensinado pela disciplina
#O loop while permite que o usuário insira novamente o valor válido, sem necessidade de rodar o código novamente

while True: #Loop se mantém até que o usuário insira um valor válido de a
    a = input("Insira um número positivo menor que 1000")
    if isintance(a, int) and b>0 and b<1000: #primeira condicional determina se o valor é valido
        break
    else: # Se não atende nossos requisitos, ele ira cair no else
        print("Número ou caracter inserido é inválido")
        
while True: #Loop se mantém até que o usuário insira um valor válido de b
    b = input("Insira um número positivo menor que 1000")
    if isintance(b, int) and b>0 and b<1000:
        break
    else:
        print("Número ou caracter inserido é inválido")
        
hipotenusa2 = (a**2 + b**2) #Calculando o quadrado da hipotenusa

print("O quadrado da hipotenusa para o triangulo retângulo com lados a={} e b={}, é {}".format(a, b, hipotenusa2))
#Aqui printamos os valores já na formatação adequada pela função format que substitui os {} pelo que foi definido

