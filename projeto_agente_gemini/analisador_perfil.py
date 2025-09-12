import os 
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
CHAVE_API_GEMINI = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=CHAVE_API_GEMINI)
modelo = "gemini-1.5-flash"

def carrega(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, "r") as arquivo:
            dados = arquivo.read()
            return dados
    except IOError as e:
        print(f"Erro: {e}")

prompt_sistema = """
"""

prompt_usuario = carrega("C:\Users\labsfiap\Desktop\Checkpoint1_PAAI_2SEM_1CCPF-main\Checkpoint1_PAAI_2SEM_1CCPF-main\dados\lista_de_compras_15_clientes.csv")

llm = genai.GenerativeModel(
    model_name = modelo,
    system_instruction = prompt_sistema
)

resposta = llm.generate_content(prompt_usuario)
print(f"Resposta path relativo: {resposta.text}")
print(f"Resposta path absoluto: {resposta.text}")
