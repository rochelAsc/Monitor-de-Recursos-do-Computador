import psutil
import time
from typing import Any, Optional

def listar_processos() -> list[dict[str, Any]]:

    processos: list[dict[str, Any]] = []
    
    for p in psutil.process_iter(['pid', 'name']):
        try:
            processos.append({
                "pid": int(p.info['pid']),
                "nome": str(p.info['name'])
            })
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            # Se o processo sumir ou não tivermos permissão só para ler o nome, ignoramos
            pass
            
    return processos

def detalhar_processo(pid: int) -> Optional[dict[str, Any]]:

    try:
        # Instancia o processo alvo
        p = psutil.Process(pid)
        
        # Coleta os dados exigidos pelo trabalho
        nome = p.name()
        status = p.status()
        memoria_bytes = p.memory_info().rss # rss = Resident Set Size (memória real em uso)
        uso_cpu = p.cpu_percent(interval=0.1) # Pausa rápida de 0.1s para medir a CPU do processo
        
        # Tempo atual - Tempo de criação = Tempo de execução em segundos
        tempo_execucao = time.time() - p.create_time()
        
        dados_processo: dict[str, Any] = {
            "nome": str(nome),
            "status": str(status),
            "uso_memoria_bytes": int(memoria_bytes),
            "uso_cpu_percentual": float(uso_cpu),
            "tempo_execucao_segundos": float(tempo_execucao)
        }
        
        return dados_processo
        
    # Tratamento de erro
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        return None