from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import joblib

import string
import nltk
from nltk.corpus import stopwords

# Isso garante que vai baixar a lista de palavras (stopwords) do inglês(E uma biblioteca util para remover palavras inuteis que IA nao vai processar)
nltk.download('stopwords', quiet=True) 

# A função que limpa o texto, que exatamente como estava no Colab(E A FUNÇÃO ENTRA AQUI: Ela ensina a IA a ignorar pontuação e palavras como "the", "is", "and")
def processaTexto(texto):
    nopunc = [char for char in texto if char not in string.punctuation]
    nopunc = ''.join(nopunc)
    cleanWords = [word for word in nopunc.split() if word.lower() not in stopwords.words('english')]
    return cleanWords

import __main__
__main__.processaTexto = processaTexto


# Inicializa o servidor da API DO fastapi
app = FastAPI(title="API de Detecção de Spam", version="1.0")

# Libera o CORS para concluir a conversar com a API(Visto que por padrão a comunicação de portas diferentes o Sistema web bloqueia por padrao)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Carrega a sua IA que fizemos o treinamento no google colab para a memória do servidor.
print("Carregando o modelo de IA...")
modelo_ia = joblib.load("modelo_ia_spam.pk")
print("Modelo carregado com sucesso!")

# Aqui vai Definir  o formato da mensagem que a API espera receber(Nesse trecho aki espera uma string)
class EmailRequest(BaseModel):
    texto: str

# AQUI ESTÁ O NOSSO  ENDPOINT QUE IREMOS INSERIR A MENSAGEM DO POSSIVEL "SPAM" OU "HAM" 
@app.post("/api/analisar")
def analisar_texto(requisicao: EmailRequest):
    # A IA lê o texto e faz a previsão(A IA Vai aplicar conceitos matematicos e algoritmos que treinamos ela)
    previsao = modelo_ia.predict([requisicao.texto])[0]
    
    # Aqui vamos criar uma variavel e associar ela o resultado Formato.Se e "spam" ou "HAM". Qualquer coisa ser nao form "SPAM" Automaticamente e "HAM"
    resultado = "SPAM" if previsao == 1 else "HAM"
    
    # Aqui iremos Devolver o JSON(Json e basicamente e padrao de comunicação entre diferentes tipos de sistema, que  bastante usado na internet)
    # vai devolver a resposta dessa comunicação json da resposta.
    return {
        "texto_analisado": requisicao.texto,
        "classificacao": resultado
    }