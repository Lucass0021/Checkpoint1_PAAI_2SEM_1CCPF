# Checkpoint 1 - Prompt And Artificial Intelligence 
**2º semestre**

Este projeto implementa um **agente de recomendação** utilizando a API **Google AI (Gemini)** em Python.
A técnica de engenharia de prompt escolhida foi a **Chain of Verification (CoVe)**, devido à sua confiabilidade na verificação de informações e na produção de recomendações seguras e bem justificadas.

---

## Como Executar

1. Clone este repositório em sua IDE.
2. Crie e ative um ambiente virtual:
```bash
python -m venv .venv
source . venv/bin/activate # Linux/Mac
.venv\Scripts\Activate     # Windows
```
3. Instale as dependências:
```bash
pip install -r requirements.txt
````
4. Configure sua chave de API Gemini:
- Crie um arquivo **.env** na raiz do projeto
- Adicione a linha:
```bash
GEMINI_API_KEY = sua_chave_aqui
```
5. Execute o agente:
```bash
python main.py
```

---
# Colaboradores
- Lucas Werpp Franco - RM: 556044
- Lucas Alves Antunes Almeida - RM: 566362
- Lucca Rosseto Rezende - RM: 564180
- Massayoshi Bando Fogaça e Silva - RM: 561779
---
