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
            pass
            
    return processos

def detalhar_processo(pid: int) -> Optional[dict[str, Any]]:

    try:
        p = psutil.Process(pid)
        
        nome = p.name()
        status = p.status()
        memoria_bytes = p.memory_info().rss # rss = Resident Set Size (memória real em uso)
        uso_cpu = p.cpu_percent(interval=0.1) # 0.1s para medir a CPU do processo
        
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

def obter_top_processos_memoria(limite: int = 5) -> list[dict[str, Any]]:

    processos: list[dict[str, Any]] = []
    
    # PID, Nome e Memória
    for p in psutil.process_iter(['pid', 'name', 'memory_info']):
        try:
            memoria_info = p.info.get('memory_info')
            rss = memoria_info.rss if memoria_info else 0 
            
            processos.append({
                "pid": int(p.info['pid']),
                "nome": str(p.info['name']),
                "memoria": int(rss)
            })
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
            
    processos_ordenados = sorted(processos, key=lambda x: x['memoria'], reverse=True)
    return processos_ordenados[:limite]


def obter_top_processos_cpu(limite: int = 5) -> list[dict[str, Any]]:

    processos: list[dict[str, Any]] = []
    
    # PID, Nome e CPU Percentual
    for p in psutil.process_iter(['pid', 'name', 'cpu_percent']):
        try:

            cpu_uso = p.info.get('cpu_percent')
            valor_cpu = cpu_uso if cpu_uso is not None else 0.0
            
            processos.append({
                "pid": int(p.info['pid']),
                "nome": str(p.info['name']),
                "cpu": float(valor_cpu)
            })
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
            
    processos_ordenados = sorted(processos, key=lambda x: x['cpu'], reverse=True)
    return processos_ordenados[:limite]