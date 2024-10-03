# def esPalindromo(texto):
#     #Convierte a minusculas y verifica alfanumericos
#     texto = "".join([caracter.lower() for caracter in frase if caracter.isalnum()])
#     #Compara texto con su reverso
#     return texto == texto[::-1]

# frase = input("Ingrese una frase: ")

# if esPalindromo(frase):
#     print(f"{frase} es un palindromo.")
# else:
#     print(f"{frase} no es un palindromo.")
    
#El siguiente codigo funciona con palabras unicas
palabra = input("Ingrese una palabra: ")
if palabra==palabra[::-1]:
    print(f"{palabra} es un palindromo.")
else:
    print(f"{palabra} no es un palindromo.")