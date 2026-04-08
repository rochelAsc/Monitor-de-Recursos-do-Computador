from typing import Any

def listar_processos() -> list[dict[str, Any]]:
    """
    Itera sobre os processos em execução no sistema operacional.
    Para otimizar o desempenho, coleta apenas o PID e o Nome.
    """
    return []

def detalhar_processo(pid: int) -> dict[str, Any] | None:
    """
    Busca informações detalhadas de um processo específico usando seu PID.
    Deve tratar erros (ex: processo não existe mais ou sem permissão de acesso).
    Retorna None se falhar na busca.
    """
    pass