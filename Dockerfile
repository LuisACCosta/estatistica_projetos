# Usa uma versão leve do Python
FROM python:3.10-slim

# Define a pasta de trabalho dentro do contêiner
WORKDIR /app

# Copia a lista de dependências e instala tudo
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o resto dos seus arquivos para dentro do contêiner
COPY . .

# Comando que o Docker vai rodar quando ligar
CMD ["python", "analise.py"]