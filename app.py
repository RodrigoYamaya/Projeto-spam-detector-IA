from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import joblib

# Inicializa o servidor da API DO fastapi
app = FastAPI(title="API de Detecção de Spam", version="2.0")

# Libera o CORS para concluir a conversar com a API(Visto que por padrão a comunicação de portas diferentes o Sistema web bloqueia por padrao)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Carrega a sua IA que fizemos o treinamento no google colab para a memória do servidor.
# OBS: O carregamento agora é instantâneo pois toda a limpeza do texto já está embutida dentro do arquivo .pk!
print("Carregando o modelo de IA...")
modelo_ia = joblib.load("modelo_ia_spam_Definitivo.pk")
print("Modelo carregado com sucesso!")

# Aqui vai Definir o formato da mensagem que a API espera receber(Nesse trecho aki espera uma string)
class EmailRequest(BaseModel):
    texto: str

# AQUI ESTÁ O NOSSO ENDPOINT QUE IREMOS INSERIR A MENSAGEM DO POSSIVEL "SPAM" OU "HAM" 
@app.post("/api/analisar")
def analisar_texto(requisicao: EmailRequest):
    
    # A IA lê o texto e faz a previsão(A IA Vai aplicar conceitos matematicos e algoritmos que treinamos ela)
    previsao = modelo_ia.predict([requisicao.texto])[0]
    
    print(f"---> ALERTA DE DEBUG: A IA respondeu: {previsao}")
    
    # Aqui vamos criar uma variavel e associar ela o resultado Formato. Se e "spam" ou "HAM". Qualquer coisa ser nao form "SPAM" Automaticamente e "HAM"
    previsao_str = str(previsao).lower()
    
    # Tratamento à prova de falhas: verifica se a resposta é 1, "spam" ou "SPAM"
    if previsao == 1 or previsao_str == "spam":
        resultado = "SPAM"
    else:
        resultado = "HAM"
            
    # Aqui iremos Devolver o JSON(Json e basicamente e padrao de comunicação entre diferentes tipos de sistema, que bastante usado na internet)
    # vai devolver a resposta dessa comunicação json da resposta.
    return {
        "texto_analisado": requisicao.texto,
        "classificacao": resultado
    }