# Projeto-spam-detector-IA

Uma API REST desenvolvida em Python para a classificação de mensagens de texto. O núcleo inteligente da aplicação é um modelo de Machine Learning otimizado (`LinearSVC`), que foi previamente treinado e exportado via Google Colab, para identificar com precisão se uma mensagem recebida é um SPAM (Fraude) ou HAM (Legítima).

## Integrantes do Grupo

| Nome | RA | E-mail | Curso |
| :--- | :--- | :--- | :--- |
| **Rodrigo Yamaya Gonçalves** | 1262324774 | rodrigoyamaya17@hotmail.com | Ciência da Computação |
| **Lucas Ottvagen** | 12624117292 | lucasottvagen@gmail.com | Ciência da Computação |
| **Luiz Felippe Almeida Veloso** | 1262326927 | luizfelippe2017@hotmail.com | Ciência da Computação |
| **David Antony Gouveia de Souza** | 1262429556 | davidantonyggg@gmail.com | Ciência da Computação |
| **Alan Pereira de Lima** | 1262422622 | alanzin121005@gmail.com | Ciência da Computação |

## Tecnologias Utilizadas

* **Backend:** FastAPI (Python)
* **Servidor:** Uvicorn
* **Machine Learning:** Scikit-Learn (`LinearSVC`, `CountVectorizer`, `TfidfTransformer`)
* **Manipulação de Dados:** Pandas
