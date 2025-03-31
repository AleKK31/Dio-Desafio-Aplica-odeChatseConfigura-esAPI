#Instalando Plugins no Semantic Kernel
## O Semantic Kernel é um sistema de plug-in, o que significa que você pode adicionar funcionalidades extras a ele.
## Por exemplo, você pode adicionar um plug-in que permite que o kernel se conecte a um banco de dados SQL,
## ou um plug-in que permite que ele se conecte a um serviço de IA específico.

from semantic_kernel import Kernel

def multiplicação(a: int, b: int) -> int:
    return a * b

kernel = Kernel()
kernel.add_function(multiplicação, "multiplicar")

resultado = kernel.invoke("multiplicar", 8, 4)
print(resultado)
