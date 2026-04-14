import psutil
from typing import Any, Optional

def obter_dados_energia() -> Optional[dict[str, Any]]:

    bateria = psutil.sensors_battery()
    
    if bateria is None:
        return None
        
    dados_energia: dict[str, Any] = {
        "nivel_bateria": float(bateria.percent),
        "conectado": bool(bateria.power_plugged)
    }
    
    return dados_energia