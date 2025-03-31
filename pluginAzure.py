#Adicionando o Plugin de Azure OpenAI Chat
## O Azure OpenAI Chat é um serviço de IA que permite que você crie assistentes de chat inteligentes.
## Com o plug-in do Azure OpenAI Chat, você pode adicionar capacidades de chatbot ao seu kernel.
from semantic_kernel import Kernel
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion

kernel = Kernel()
kernel.add_service(
    AzureChatCompletion(
        service_id="openai-chat-plugin",
        deployment_name="gpt-4",
        endpoint="https://seu-endpoint.openai.azure.com/",
        api_key="sua-chave-api"
    )
)

def chat_with_ai(user_input: str):
    response = kernel.chat(user_input)
    return response

entrada = "Explique como posso criar uma linguagem de programação de alto nível."
saida = chat_with_ai(entrada)
print(f"Entrada: {entrada}")
print(f"Saída: {saida}")
