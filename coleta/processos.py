def listar_processos() -> list[dict]:
    """
    Itera sobre os processos em execução no sistema operacional
    Para otimizar o desempenho, coleta apenas o PID e o Nome
    """
    pass

def detalhar_processo(pid: int) -> dict | None:
    """
    Busca informações detalhadas de um processo específico usando seu PID
    Deve tratar erros (ex: processo não existe mais ou sem permissão de acesso)
    Retorna None se falhar na busca
    """
    pass