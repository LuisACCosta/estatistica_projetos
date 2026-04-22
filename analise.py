import pandas as pd

# 1. Configurações iniciais
ARQUIVO = 'sua_pesquisa.csv'


# 2. Carregando os dados
try:
    df = pd.read_csv(ARQUIVO)
    print("✅ Arquivo carregado com sucesso!")
except FileNotFoundError:
    print(f"❌ Erro: O arquivo '{ARQUIVO}' não foi encontrado na pasta.")
    exit()

df = df.rename(columns={
    'Qual é a idade do(a) seu/sua filho(a)? > (Nota: Se você tiver mais de um filho, por favor, responda o questionário pensando naquele cujo uso de internet mais preocupa você no momento, ou preencha novamente para cada filho).':'idade',
    
})

col_idade   = ...
col_impacto = ...
col_pagar   = ...
col_valor   = ...

# 3. Verificação inicial
print("\n--- Categorias de Idade encontradas ---")
print(df[col_idade].unique())

# 4. Filtragem de Dados
idades_validas = ['0 a 5 anos', '6 a 9 anos', '10 a 13 anos', '14 a 17 anos']
df_filtrado = df[df[col_idade].isin(idades_validas)].copy()

print(f"\nRespostas totais: {len(df)}")
print(f"Respostas válidas após filtro: {len(df_filtrado)}")

# 5. Análise Estatística
print("\n" + "="*30)
print(" RESULTADOS DA ANÁLISE ")
print("="*30)

print("\n📊 Distribuição por faixa etária:")
print(df_filtrado[col_idade].value_counts())

print("\n🧠 Percepção de impacto:")
print(df_filtrado[col_impacto].value_counts())

print("\n💰 Disposição para pagar (%):")
print(df_filtrado[col_pagar].value_counts(normalize=True).mul(100).round(1).astype(str) + '%')

# 6. Análise de Preço
df_pagantes = df_filtrado[df_filtrado[col_pagar].str.contains('Sim|pagaria', case=False, na=False)]

print("\n💵 Valor mensal ideal (entre interessados):")
if not df_pagantes.empty:
    print(df_pagantes[col_valor].value_counts())
else:
    print("Nenhum registro de intenção de pagamento encontrado.")