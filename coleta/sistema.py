import psutil
import datetime
from typing import Any, Optional

def obter_dados_sistema() -> dict[str, Any]:
    
    # Tempo desde o Boot do Sistema
    boot_timestamp = psutil.boot_time()
    # Converte o timestamp para uma string legível
    boot_data = datetime.datetime.fromtimestamp(boot_timestamp).strftime("%d/%m/%Y %H:%M:%S")
    
    # Usuários Conectados
    usuarios = [str(u.name) for u in psutil.users()]
    
    # Temperatura do Sistema (Pode não estar disponível em todos os sistemas)
    temperatura_media: Optional[float] = None
    if hasattr(psutil, "sensors_temperatures"):
        temps = psutil.sensors_temperatures()
        if temps:
            # Pega a primeira chave de sensor disponível e lê a temperatura atual
            nome_sensor = list(temps.keys())[0]
            temperatura_media = float(temps[nome_sensor][0].current)
            
    dados_sistema: dict[str, Any] = {
        "boot": str(boot_data),
        "usuarios": usuarios, # Lista de strings
        "temperatura": temperatura_media # Float ou None
    }
    
    return dados_sistema