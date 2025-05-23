# uerrbot/bot.py
import os
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from langchain_community.document_loaders import WebBaseLoader

class UerrBot:
    def __init__(self, api_key=None, model="llama3-70b-8192"):
        if api_key:
            os.environ["GROQ_API_KEY"] = api_key
        self.chat = ChatGroq(model=model)

    def carregar_documentos(self, url):
        loader = WebBaseLoader(url)
        return loader.load()

    def concatenar_conteudo(self, lista_documentos):
        return " ".join(doc.page_content for doc in lista_documentos)

    def construir_chain(self):
        template = ChatPromptTemplate.from_messages([
            {"role": "system", "content": "Você é um assistente chamado Asimov e acessa informações fornecidas para responder perguntas."},
            {"role": "user", "content": "Com base nas informações extraídas do site, responda a pergunta\n\n {pergunta}\n\n{documentos_informados}"}
        ])
        return template | self.chat

    def perguntar(self, documentos_informados, pergunta):
        chain = self.construir_chain()
        resposta = chain.invoke({
            "documentos_informados": documentos_informados,
            "pergunta": pergunta,
            "input": pergunta
        })
        return resposta.content
