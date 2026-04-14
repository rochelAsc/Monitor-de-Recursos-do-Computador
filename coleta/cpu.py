import psutil
from typing import Any

def obter_dados_cpu() -> dict[str, Any]:

    n_logicos = psutil.cpu_count(logical=True)
    n_fisicos = psutil.cpu_count(logical=False)
    
    uso_percentual = psutil.cpu_percent(interval=1)
    
    dados_cpu: dict[str, Any] = {
        "nucleos_logicos": int(n_logicos) if n_logicos is not None else 0,
        "nucleos_fisicos": int(n_fisicos) if n_fisicos is not None else None,
        "percentual_uso": float(uso_percentual)
    }
    
    return dados_cpu