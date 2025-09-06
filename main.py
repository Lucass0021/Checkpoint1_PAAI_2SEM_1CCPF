import os
import google.generativeai as genai
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()
CHAVE_API_KEY = os.getenv("GEMINI_API_KEY")

# Configurar API
genai.configure(api_key=CHAVE_API_KEY)

# Modelo escolhido
MODELO_ESCOLHIDO = "gemini-1.5-flash"
prompt_sistema = """
Você é um assistente profissional e neutro especializado em recomendações nas áreas médica e jurídica,
usando a técnica Chain of Verification (CoVe).

Regras obrigatórias:
1) NÃO adote persona lúdica ou teatral (por exemplo: "agente secreto"). Seja sempre neutro e profissional.
2) Faça uma verificação breve (1 frase) e uma recomendação final curta (máx. 2 frases / ~35 palavras).
3) Estruture a resposta em duas linhas curtas:
   Verificação: <uma frase curta>
   Recomendação: <uma ou duas frases curtas>
4) Sempre inclua, ao fim, uma única frase curta de aviso: "Consulte um profissional para orientação definitiva."
5) Em medicina/jurídico, evite diagnósticos/pareceres definitivos e não dê instruções perigosas.
"""

# Técnica de Engenharia de Prompt: Chain of Verification (CoVe)
# Vantagem: Confiabilidade em Dados e Fatos
# Recomendado para: Informações Críticas (Médicas, Legais), fact-checking, relatórios técnicos


llm = genai.GenerativeModel(
    model_name=MODELO_ESCOLHIDO,
    system_instruction=prompt_sistema
)

print("=== Chat com Gemini ===")
print("Digite 'sair' para encerrar.\n")

while True:
    pergunta = input("\nInsira um texto: \n")

    if pergunta.lower() in ["sair", "exit", "quit"]:
        print("Encerrando o chat. Até mais!")
        break

    resposta = llm.generate_content(pergunta)
    print(f"\nResposta: {resposta.text}\n")
