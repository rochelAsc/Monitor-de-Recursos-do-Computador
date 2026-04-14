from typing import Any, Optional
from utilidades.formatacao import converter_bytes, formatar_tempo

def exibir_cpu(dados_cpu: dict[str, Any]) -> None:

    print("\n" + "="*30)
    print("=== MONITOR DE CPU ===")
    print("="*30)
    
    n_fisicos = dados_cpu.get("nucleos_fisicos")
    
    # Exibe núcleos físicos apenas quando disponível
    if n_fisicos is not None:
        print(f"Núcleos Físicos : {n_fisicos}")
        
    print(f"Núcleos Lógicos : {dados_cpu['nucleos_logicos']}")
    print(f"Uso Atual       : {dados_cpu['percentual_uso']:.1f}%")


def exibir_memoria(dados_memoria: dict[str, Any]) -> None:

    print("\n" + "="*30)
    print("=== MONITOR DE MEMÓRIA ===")
    print("="*30)
    
    total = converter_bytes(dados_memoria['total'])
    em_uso = converter_bytes(dados_memoria['em_uso'])
    disponivel = converter_bytes(dados_memoria['disponivel'])
    
    print(f"Total      : {total}")
    print(f"Em Uso     : {em_uso}")
    print(f"Disponível : {disponivel}")
    print(f"Uso (%)    : {dados_memoria['percentual']:.1f}%")


def exibir_energia(dados_energia: Optional[dict[str, Any]]) -> None:

    print("\n" + "="*30)
    print("=== MONITOR DE ENERGIA ===")
    print("="*30)
    
    if dados_energia is None:
        print("[!] Informação de bateria não disponível nesta máquina.")
    else:
        status_tomada = "Sim" if dados_energia['conectado'] else "Não"
        print(f"Bateria Restante  : {dados_energia['nivel_bateria']:.1f}%")
        print(f"Conectado à rede  : {status_tomada}")


def exibir_lista_processos(lista_processos: list[dict[str, Any]]) -> None:

    print("\n" + "="*40)
    print("=== LISTA DE PROCESSOS (Top 15) ===")
    print("="*40)
    print(f"{'PID':<10} | {'NOME DO PROCESSO'}")
    print("-" * 40)
    
    # Limita a 15 para não floodar o terminal com centenas de linhas
    for proc in lista_processos[:15]:
        print(f"{proc['pid']:<10} | {proc['nome']}")
    print("...")


def exibir_detalhes_processo(dados_processo: Optional[dict[str, Any]]) -> None:

    print("\n" + "="*40)
    print("=== DETALHES DO PROCESSO ===")
    print("="*40)
    
    if dados_processo is None:
        print("[!] Processo não encontrado, encerrado ou acesso negado.")
    else:
        memoria_legivel = converter_bytes(dados_processo['uso_memoria_bytes'])
        tempo_legivel = formatar_tempo(dados_processo['tempo_execucao_segundos'])
        
        print(f"Nome      : {dados_processo['nome']}")
        print(f"Status    : {dados_processo['status']}")
        print(f"Memória   : {memoria_legivel}")
        print(f"CPU       : {dados_processo['uso_cpu_percentual']:.1f}%")
        print(f"Tempo Exec: {tempo_legivel}")