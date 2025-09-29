

while True:
    
    senha = input("Digite uma senha: ")
    
    oito_digitos = len(senha) >= 8
    maiuscula = False
    numero = False
    
    
    
    for caractere in senha:
        if caractere.isupper():
            maiuscula = True
        if caractere.isdigit():
            numero = True
            
    if oito_digitos and maiuscula and numero:
        print("Senha valida! Atende a todos os requisitos!")
        break
    elif not oito_digitos:
        print("Senha Inválida. A senha deve ter no mínimo 8 caracteres.")
    elif not maiuscula:
        print("Senha Inválida. A senha deve conter pelo menos uma letra maiúscula.")
    else:
        print("Senha Inválida. A senha deve conter pelo menos um número.")
        
        