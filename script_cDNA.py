#Exercicio 4 - script_cDNA.py

import sys # Inicialmente importamos o modulo sys

dna = sys.argv[1]  # utilizamos da função sys.argv para possibilitar ao usuario que incira argumentos para efetuar as proximas operações
try:
    n1 = int(sys.argv[2])
    n2 = int(sys.argv[3])
    n3 = int(sys.argv[4])
    n4 = int(sys.argv[5])


    if n4>len(dna): #Criei uma condicional com if
        print('Erro! N4 é maior que o comprimento da sequência!")    # Adicionei uma condição de erro, que é quando o N4 é maior que o comprimento da sequencia
    else: # Se a condição de erro não for atendida a operação ira continuar
        cds1 = ''
        cds2 = ''

        if dna[(n1 - 1):(n1+2)] == 'ATG': # Adicionei a condição que n1 deve ser iniciado com ATG
            cds1 = dna[(n1-1):(n2)]

        if dna[(n4 - 3):(n4)] in ['TAG', 'TAA', 'TGA']: #Adicionei a condição para n4 terminar com TAG, TAA, ou TGA
            cds2 = dna[(n3-1):(n4)]
    
        if cds1 != '' and cds2 != '':
            string_final = cds1 + cds2 #Junto os dois fragmentos de DNA que obedecem as minhas condições
            print(string_final) #Printo as duas sequencias juntas (minha sequencia final)
        
except ValueError:
    print("Um dos valores de 'n' inseridos não é um número inteiro") #Adiciono mais uma condição para que o programa avise ao usuario se o valor inserido para n não é um int. O valor dos n precisa ser numerico
