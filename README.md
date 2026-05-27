# Projeto-spam-detector-IA

Uma API REST desenvolvida em Python para a classificação de mensagens de texto. O núcleo inteligente da aplicação é um modelo de Machine Learning otimizado (`LinearSVC`), que foi previamente treinado e exportado via Google Colab, para identificar com precisão se uma mensagem recebida é um SPAM (Fraude) ou HAM (Legítima).


## Tecnologias Utilizadas

* **Backend:** FastAPI (Python)
* **Servidor:** Uvicorn
* **Machine Learning:** Scikit-Learn (`LinearSVC`, `CountVectorizer`, `TfidfTransformer`)
* **Manipulação de Dados:** Pandas

# Comando para Instalar as dependências

python -m pip install -r requirements.txt


# Iniciar O servidor Backend

python -m uvicorn app:app --reload
