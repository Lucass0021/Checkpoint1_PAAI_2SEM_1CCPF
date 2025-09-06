# Importando Bibliotecas
import os 
import google.generativeai as genai
from dotenv import load_dotenv

# Carregando variáveis de ambiente
load_dotenv()
CHAVE_API_KEY = os.getenv("GEMINI_API_KEY")

# Configurando API
genai.configure(api_key=CHAVE_API_KEY)

# Modelo escolhido
MODELO_ESCOLHIDO = "gemini-1.5-flash"
prompt_sistema = """
Você está utilizando a técnica de engenharia de prompt "Chain of Verification" (CoVe). 
Sua principal função é garantir a veracidade e a confiabilidade das informações que você fornece. 
Sempre que responder a uma pergunta, faça uma verificação interna para confirmar a precisão das informações, 
especialmente quando tratar de tópicos críticos como médicos, legais ou dados técnicos. 
Em caso de dúvida, forneça as fontes ou avise que não tem informações verificadas.

Suas respostas devem ser breves e diretas.
"""

# Técnica de Engenharia de Prompt: Chain of Verification ("CoVe")
# Vantagem: Confiabilidade em fatos e dados
# Recomendado para: Informações críticas (Médicas/Legais), fact-checking, relatórios técnicos


llm = genai.GenerativeModel(
    model_name=MODELO_ESCOLHIDO, 
    system_instruction=prompt_sistema
)

print("=== CHAT COM GEMINI ===")
print("Digite 'sair' para encerrar.\n")

while True:
    pergunta = input("Insira um texto: \n")

    if pergunta.lower() in ['sair', 'exit', 'quit']:
        print("Encerrando o chat, até mais!")
        break
    else:
        resposta = llm.generate_content(pergunta)
        print(f"\nResposta gerada,: {resposta.text}\n")