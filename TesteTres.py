import json

faturamento_json = '''[
    {"dia": 1, "valor": 22174.1664},
    {"dia": 2, "valor": 24537.6698},
    {"dia": 3, "valor": 26139.6134},
    {"dia": 4, "valor": 0.0},
    {"dia": 5, "valor": 0.0},
    {"dia": 6, "valor": 26742.6612}
]'''

faturamento = json.loads(faturamento_json)
faturamento_validos = [dia['valor'] for dia in faturamento if dia['valor'] > 0]

menor_faturamento = min(faturamento_validos)
maior_faturamento = max(faturamento_validos)
media_mensal = sum(faturamento_validos) / len(faturamento_validos)
dias_acima_media = len([valor for valor in faturamento_validos if valor > media_mensal])

print(f"Menor faturamento: {menor_faturamento:.2f}")
print(f"Maior faturamento: {maior_faturamento:.2f}")
print(f"Dias com faturamento acima da média: {dias_acima_media}")
