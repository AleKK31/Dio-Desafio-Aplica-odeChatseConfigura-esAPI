# Desafio - Aplicações e Configurações com Azure OpenAI

Este repositório contém exemplos de uso do **Semantic Kernel** e integração com o **Azure OpenAI**. Abaixo está uma descrição de cada arquivo presente no projeto.

Os códigos de exemplos foram feitos em Python, mas podem ser feitos em .NET ou Java.

## Arquivos

### `criandoKernel.py`
Este arquivo apresenta como criar e configurar um kernel básico utilizando o **Semantic Kernel**. Ele inclui:
- Configuração do kernel com o serviço Azure OpenAI.
- Exemplo de interação com o modelo para responder à pergunta: "O que é e como funciona o Semantic Kernel?".

### `instalandoPlugins.py`
Este arquivo mostra como adicionar funcionalidades extras ao **Semantic Kernel** por meio de plugins. Ele inclui:
- Um exemplo de função personalizada chamada `multiplicação`.
- Demonstração de como registrar e invocar a função no kernel.

### `pluginAzure.py`
Este arquivo demonstra como configurar e utilizar o **Azure OpenAI Chat** como um serviço no **Semantic Kernel**. Ele inclui:
- Configuração do serviço Azure OpenAI Chat.
- Função `chat_with_ai` para interagir com o modelo GPT-4.
- Exemplo de entrada e saída de uma interação com o modelo.

## Requisitos
- Python
- Biblioteca `semantic-kernel` instalada. Para instalar, execute:
  ```bash
  pip install semantic-kernel
  ```

## Como Executar
1. Configure o arquivo com suas credenciais do Azure OpenAI (`endpoint` e `api_key`).
2. Execute os scripts Python conforme necessário:
   ```bash
   python pluginAzure.py
   python instalandoPlugins.py
   python criandoKernel.py
   ```

## Links Úteis
- [Documentação do Semantic Kernel](https://github.com/microsoft/semantic-kernel)
- [Azure OpenAI](https://azure.microsoft.com/en-us/products/cognitive-services/openai-service/)
