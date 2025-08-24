altura = float(input("Digite sua altura em etros ex. 1.75: "))
sexo = input("M para masculino e F para feinino ")

if (sexo == "M" or sexo == "m"):
    peso_ideal = (72.7 * altura) - 58 
    print(" Seu peso ideal é: {:.2f}".format(peso_ideal))          
else:
    peso_ideal = (62.1 * altura) - 44.7
    print(" Seu peso ideal é: {:.2f}".format(peso_ideal))