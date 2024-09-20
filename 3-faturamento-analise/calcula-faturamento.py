import json


def calcular_faturamento(dados_faturamento_diario):
    # Filtra apenas os dias com faturamento positivo
    valores_positivos = [dia["valor"] for dia in dados_faturamento_diario if dia["valor"] > 0]

    # Verifica se existem valores positivos para evitar erros no cálculo
    if not valores_positivos:
        return None, None, 0  # Retorna valores nulos se não houver faturamento positivo

    # Calcula as métricas
    menor_faturamento = min(valores_positivos)
    maior_faturamento = max(valores_positivos)
    media_mensal = sum(valores_positivos) / len(valores_positivos)
    dias_acima_da_media = len([valor for valor in valores_positivos if valor > media_mensal])

    return menor_faturamento, maior_faturamento, dias_acima_da_media


if __name__ == "__main__":
    try:
        # Lê o arquivo JSON
        with open('faturamento.json', 'r') as file:
            dados_faturamento = json.load(file)

        # Verifica se o campo "faturamento" existe no JSON
        if "faturamento" not in dados_faturamento:
            raise KeyError("O campo 'faturamento' não foi encontrado no arquivo JSON.")

        # Extrai os dados de faturamento diário
        faturamento_diario = dados_faturamento["faturamento"]

        # Chama a função de cálculo e imprime os resultados
        menor, maior, dias_acima_media = calcular_faturamento(faturamento_diario)

        if menor is not None and maior is not None:
            print(f"Menor faturamento: R$ {menor:.2f}")
            print(f"Maior faturamento: R$ {maior:.2f}")
            print(f"Dias com faturamento acima da média: {dias_acima_media}")
        else:
            print("Não houve dias com faturamento positivo.")

    except FileNotFoundError:
        print("Arquivo 'faturamento.json' não encontrado.")
    except json.JSONDecodeError:
        print("Erro ao decodificar o arquivo JSON.")
    except KeyError as e:
        print(f"Erro: {str(e)}")
