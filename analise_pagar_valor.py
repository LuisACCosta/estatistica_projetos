from utils import preparar_dados

# 1. Configurações iniciais
ARQUIVO = 'sua_pesquisa.csv'

# 2. Carregando os dados da nossa fábrica
df = preparar_dados(ARQUIVO)

# 3. Filtragem de Dados (O Chapéu do Cientista de Dados)
# Vamos identificar quem NÃO quer pagar usando uma busca por texto parcial para evitar erros de digitação/espaços
filtro_nao_pagaria = df['pagar'].str.contains('Não pagaria', case=False, na=False)

# O símbolo '~' inverte o filtro. Ou seja: me dê todos que NÃO estão na lista de quem não pagaria.
df_potenciais_clientes = df[~filtro_nao_pagaria].copy()

print("\n" + "="*55)
print(" 🕵️‍♀️ ANÁLISE DE POTENCIAIS CLIENTES (PAGANTES) ")
print("="*55)

print(f"\n📊 Tamanho da Amostra:")
print(f"  -> Total de respostas originais: {len(df)}")
print(f"  -> Clientes em potencial (filtrados): {len(df_potenciais_clientes)}")

# 4. Análise de Comportamento (O Chapéu do Cientista Social)
print("\n🧠 Esforço de Controle (Apenas entre potenciais clientes):")
contagem_controle = df_potenciais_clientes['tenta_controlar'].value_counts()
pct_controle = df_potenciais_clientes['tenta_controlar'].value_counts(normalize=True).mul(100).round(1)

for resposta, qtd in contagem_controle.items():
    print(f"  -> {resposta}: {qtd} pessoas ({pct_controle[resposta]}%)")

# 5. Análise de Preço (O Chapéu do Estatístico)
print("\n💰 Distribuição de Valor Mensal Ideal:")
contagem_valor = df_potenciais_clientes['valor'].value_counts()
pct_valor = df_potenciais_clientes['valor'].value_counts(normalize=True).mul(100).round(1)

for resposta, qtd in contagem_valor.items():
    print(f"  -> {resposta}: {qtd} respostas ({pct_valor[resposta]}%)")

print("\n" + "="*55)