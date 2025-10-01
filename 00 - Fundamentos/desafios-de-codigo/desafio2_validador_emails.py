

# Entrada do usuário
email = input().strip()

def validador_email(email):
    if ' ' not in email and not email.startswith('@') and ("@gmail.com" in email or "@outlook.com" in email):
        return "E-mail válido"
    else:
        return "E-mail inválido"

print (validador_email(email))