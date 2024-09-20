def inverter_string(texto):
    # Inicializa uma string vazia para armazenar o resultado
    invertida = ""

    # Itera sobre a string original de trás para frente
    for i in range(len(texto) - 1, -1, -1):
        invertida += texto[i]

    return invertida


if __name__ == "__main__":
    # Entrada do usuário
    texto = input("Digite uma string para inverter: ")

    # Chama a função e exibe o resultado
    texto_invertido = inverter_string(texto)
    print(f"String invertida: {texto_invertido}")
