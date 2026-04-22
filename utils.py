import pandas as pd
import sys

def preparar_dados(caminho_arquivo):
    # 1. Tentativa de carregamento
    try:
        df = pd.read_csv(caminho_arquivo)
        print("✅ Dados brutos carregados com sucesso!")
    except FileNotFoundError:
        print(f"❌ Erro: O arquivo '{caminho_arquivo}' não foi encontrado.")
        sys.exit()

    # 2. Renomeando as colunas (mapeando a pergunta inteira para um nome curto)
    # Dica: Mantive os espaços exatos que você mandou para não dar erro
    df = df.rename(columns={
        'Qual é a idade do(a) seu/sua filho(a)? > (Nota: Se você tiver mais de um filho, por favor, responda o questionário pensando naquele cujo uso de internet mais preocupa você no momento, ou preencha novamente para cada filho).': 'idade',
        'O(a) seu/sua filho(a) utiliza redes sociais ou aplicativos de vídeos (como YouTube, TikTok, Instagram, etc.)? ': 'usa_redes',
        'Em uma escala de 1 a 5, onde 1 é "usa muito", 5 é "usa pouco" e 3 é "de forma equilibrada", o quanto seu filho usa essas plataformas?  ': 'escala_uso',
        'Você percebe algum impacto das redes sociais no comportamento, pensamentos e ações do(a) seu/sua filho(a)? Se sim, como você classificaria esse impacto?': 'impacto',
        'Se o impacto foi negativo, você acha que ele está mais relacionado a:  ': 'causa_impacto',
        'Você tenta controlar o que seu filho consome nas redes sociais?  ': 'tenta_controlar',
        'Em uma escala de 1 a 5, onde 1 é " Nenhum sucesso / Não consigo controlar" e 5 é "Total sucesso / Controlo perfeitamente "qual o seu nível de sucesso ao tentar controlar esse conteúdo?  ': 'sucesso_controle',
        'Qual é a sua experiência atual com aplicativos ou ferramentas de controle parental (ex: Family Link, Qustodio, etc.)?  ': 'experiencia_controle',
        'Você estaria disposto(a) a pagar por uma solução que filtre de forma eficiente conteúdos que possam ser uma má influência para o seu filho?  ': 'pagar',
        'Qual valor mensal você considera o ideal para assinar essa solução de segurança digital?  ': 'valor'
    })


    
    
    # 3. Exportando a tabela pronta!
    return df