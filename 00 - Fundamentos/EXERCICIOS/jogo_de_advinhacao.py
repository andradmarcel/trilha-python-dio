

import random




print("--- Jogo de Adivinhação ---")
print("Tente adivinhar o número secreto. Você tem 7 vidas!")

while True:
    numero_secreto = random.randint(1,100)
    # numero_secreto = 20
    tentativas = 7 
    
    while True:
        try:
            print(f"Voce tem {tentativas} vidas")
            palpite = int(input("Digite um numero entre 1 a 100: "))            
    
            if palpite < numero_secreto:
                print("Quase acertou! Mas o numero é maior do que voce digitou!")
                tentativas -= 1
            elif palpite > numero_secreto:
                print("Quase acertou! Mas o numero é menor do que voce digitou!")
                tentativas -= 1
            else:
                print(f"\nACERTOU, MISERAVI! O número era {numero_secreto}!")
                break
            
            if tentativas == 0:
                print(f"\nFIM DE JOGO! Suas vidas acabaram. O número secreto era {numero_secreto}.")
                break
        except ValueError:
            print("Entrada inválida! Por favor, digite um número inteiro.")    
            
    continuar = input("\nDeseja jogar novamente? [s/n]: ")        
    resposta_formatada = continuar.lower().strip()        
    if resposta_formatada == "s" or resposta_formatada == "sim":
        continue 
    else:
        print("Obrigado por jogar!")
        break        
                        
        
    