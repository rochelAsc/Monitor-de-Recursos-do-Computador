from typing import Any
import psutil

def obter_dados_memoria() -> dict[str, Any]:
    
    memoria = psutil.virtual_memory()
    
    dados_memoria: dict[str, Any] = {
        "total": int(memoria.total),
        "em_uso": int(memoria.used),
        "disponivel": int(memoria.available),
        "percentual": float(memoria.percent)
    }
    
    return dados_memoria