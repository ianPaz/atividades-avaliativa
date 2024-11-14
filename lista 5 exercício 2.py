def gerenciar_clientes(clientes_A, clientes_B):
    # A. Identificar os clientes que estão em ambos 
    clientesNosDois = clientes_A & clientes_B
    print("Clientes em ambos os conjuntos:", clientesNosDois)
    
    # B. Identificar os clientes que estão apenas em clientes_A 
    clientesA = clientes_A - clientes_B
    print("Clientes apenas em clientes_A:", clientesA)
    
    # C. Identificar os clientes que estão em apenas um 
    clientes_unicos = clientes_A ^ clientes_B
    print("Clientes que estão apenas em um dos conjuntos:", clientes_unicos)
    
    # D. Calcular a porcentagem de clientes únicos
    todos_clientes = clientes_A | clientes_B  
    total_clientes_unicos = len(todos_clientes)  # Quantidade de clientes únicos
    total_clientes_A_e_B = len(clientes_A) + len(clientes_B)  # Total de clientes somando ambos os conjuntos
    
    # Cálculo da porcentagem de clientes únicos
    if total_clientes_A_e_B > 0:
        porcentagem_unicos = (total_clientes_unicos / total_clientes_A_e_B) * 100
    else:
        porcentagem_unicos = 0  #Caso não haja clientes 
    
    # Exibe a porcentagem de clientes únicos
    print(f"Porcentagem de clientes únicos: {porcentagem_unicos:.2f}%")
    

# Conjuntos fornecidos de clientes A e B
clientes_A = {"Alice", "Bob", "Charlie", "David"}
clientes_B = {"Charlie", "David", "Eve", "Frank"}

# Chama a função para gerenciar os conjuntos
gerenciar_clientes(clientes_A, clientes_B)
