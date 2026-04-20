import psutil
from typing import Any

def obter_dados_disco() -> list[dict[str, Any]]:

    particoes_info: list[dict[str, Any]] = []
    
    # Itera sobre todas as partições
    for part in psutil.disk_partitions(all=False):
        try:
            # Tenta acessar os dados de uso daquela partição específica
            uso = psutil.disk_usage(part.mountpoint)
            
            particoes_info.append({
                "dispositivo": str(part.device), # Ex: "C:\ para windows" ou "/dev/sda1 em sistemas linux"
                "ponto_montagem": str(part.mountpoint),
                "sistema_arquivos": str(part.fstype),
                "total": int(uso.total),
                "em_uso": int(uso.used),
                "livre": int(uso.free),
                "percentual": float(uso.percent)
            })
        except PermissionError:
            pass
            
    return particoes_info