#Criando kernel
## Permite a integração de modelos de IA, como aqueles do Azure OpenAI, em aplicações do mundo real. 
## Ele combina capacidades de IA generativa com execução de código, 
## memória e planejamento para permitir a criação de assistentes inteligentes e fluxos de trabalho automatizados.

from semantic_kernel import Kernel
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion

kernel = Kernel()
kernel.add_service(
    AzureChatCompletion(
        service_id="my-openai-service",
        deployment_name="gpt-4",
        endpoint="https://seu-endpoint.openai.azure.com/",
        api_key="sua-chave-api"
    )
)

response = kernel.chat("O que é e como funciona o Semantic Kernel?")
print(response)
