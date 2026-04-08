from typing import Any

def exibir_cpu(dados_cpu: dict[str, Any]) -> None:
    """
    Recebe o dicionário de CPU rigorosamente tipado e o imprime
    """
    pass

def exibir_memoria(dados_memoria: dict[str, Any]) -> None:
    """
    Recebe o dicionário de memória rigorosamente tipado e o exibe
    """
    pass

def exibir_energia(dados_energia: dict[str, Any] | None) -> None:
    """
    Recebe os dados de bateria. O Pylance obrigará a checagem 
    de None antes de acessar os dados do dicionário
    """
    pass

def exibir_lista_processos(lista_processos: list[dict[str, Any]]) -> None:
    """
    Recebe a lista de processos, onde cada item é um dicionário 
    com chaves em string e valores mistos
    """
    pass

def exibir_detalhes_processo(dados_processo: dict[str, Any] | None) -> None:
    """
    Recebe os detalhes de um processo. O Pylance obrigará a 
    checagem de None (caso o processo não tenha sido encontrado)
    """
    pass