import psutil
import socket
from typing import Any

def obter_dados_rede() -> list[dict[str, Any]]:

    interfaces_info: list[dict[str, Any]] = []
    
    # Busca os endereços lógicos e os contadores de tráfego físico
    enderecos_rede = psutil.net_if_addrs()
    contadores_io = psutil.net_io_counters(pernic=True)
    
    # Itera sobre cada placa de rede registrada no sistema
    for nome_interface, enderecos in enderecos_rede.items():
        ip = "Desconhecido"
        
        # Filtra a lista de endereços da placa para pegar apenas o IPv4
        for endereco in enderecos:
            if endereco.family == socket.AF_INET:
                ip = str(endereco.address)
                break
                
        # Pega os bytes de envio/recebimento se a placa tiver registrado tráfego
        enviados = 0
        recebidos = 0
        if nome_interface in contadores_io:
            enviados = int(contadores_io[nome_interface].bytes_sent)
            recebidos = int(contadores_io[nome_interface].bytes_recv)
            
        interfaces_info.append({
            "interface": str(nome_interface),
            "ip": ip,
            "bytes_enviados": enviados,
            "bytes_recebidos": recebidos
        })
        
    return interfaces_info