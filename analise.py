from utils import preparar_dados

# 1. Configurações iniciais
ARQUIVO = 'sua_pesquisa.csv'

# 2. Carregando os dados da nossa fábrica (utils.py)
df = preparar_dados(ARQUIVO)

# 3. Checagem de Saúde dos Dados
print("\n" + "="*40)
print(" VERIFICAÇÃO INICIAL DOS DADOS ")
print("="*40)

print(f"\n✅ Total de respostas carregadas: {len(df)}")

print("\n📋 Nomes das colunas padronizadas disponíveis para uso:")
for coluna in df.columns:
    print(f"  -> {coluna}")

print("\n" + "="*40)
print("Tudo certo! Base pronta para iniciar as análises específicas.")