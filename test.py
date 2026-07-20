# test 1
# from langchain_ollama import OllamaLLM

# llm = OllamaLLM(model="tinyllama")  # or "llama3.2"
# response = llm.invoke("Hello! i am Kiran, how are you?")
# print(response)

# test 2
# test_ollama.py
from langchain_ollama import OllamaLLM

try:
    llm = OllamaLLM(model="llama3.2")  # or whatever model you have
    response = llm.invoke("Say hello")
    print("Ollama working:", response)
except Exception as e:
    print("Ollama error:", e)