# Contadores
excelente = 0
bom = 0
ruim = 0

# Repetição para 50 entrevistados
for i in range(50):
    print("Entrevistado número", i + 1)
    
    nome = input("Digite o nome: ")
    idade = input("Digite a idade: ")
    
    print("1 - EXCELENTE")
    print("2 - BOM")
    print("3 - RUIM")
    opiniao = input("Digite sua opinião: ")
    
    # Verificando a opinião
    if opiniao == "1":
        excelente = excelente + 1
    elif opiniao == "2":
        bom = bom + 1
    elif opiniao == "3":
        ruim = ruim + 1
    else:
        print("Opinião inválida.")

# Mostrando os resultados
print("Quantidade de EXCELENTE:", excelente)
print("Quantidade de BOM:", bom)
print("Quantidade de RUIM:", ruim)