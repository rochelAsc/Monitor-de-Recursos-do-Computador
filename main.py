import os
import time
from typing import Callable, Any
from coleta.cpu import obter_dados_cpu
from coleta.memoria import obter_dados_memoria
from coleta.energia import obter_dados_energia
from coleta.processos import (listar_processos, detalhar_processo, 
                              obter_top_processos_memoria, obter_top_processos_cpu)
from coleta.sistema import obter_dados_sistema
from coleta.disco import obter_dados_disco
from coleta.rede import obter_dados_rede

from visao.terminal import (exibir_cpu, exibir_memoria, exibir_energia, 
                            exibir_lista_processos, exibir_detalhes_processo,
                            exibir_sistema, exibir_disco, exibir_rede,
                            exibir_top_processos_memoria, exibir_top_processos_cpu)

def monitorar_em_tempo_real(funcao_coleta: Callable[..., Any], funcao_exibir: Callable[..., Any], intervalo: int = 1) -> None:
    try:
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            
            dados = funcao_coleta()
            funcao_exibir(dados)
            
            print(f"\n[ Atualizando a cada {intervalo}s. Pressione Ctrl+C para voltar ao menu principal ]")
            
            time.sleep(intervalo)
            
    except KeyboardInterrupt:
        print("\nVoltando ao menu principal...")
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')

def exibir_menu() -> None:
    print("\n" + "="*45)
    print("  FERRAMENTA DE DIAGNÓSTICO DO SO (AO VIVO)  ")
    print("="*45)
    print("1. Consultar Processador (CPU)")
    print("2. Consultar Memória RAM")
    print("3. Consultar Energia/Bateria")
    print("4. Listar Processos em Execução")
    print("5. Detalhar Processo por PID")
    print("6. Informações do Sistema (Boot/Temp)")
    print("7. Monitor de Armazenamento (Discos)")
    print("8. Monitor de Rede (Tráfego/IP)")
    print("9. Top 5 Processos (Mais Memória)")
    print("10. Top 5 Processos (Mais CPU)")
    print("0. Sair do Programa")
    print("="*45)

def main() -> None:
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção numérica: ")
        
        if opcao == '1':
            monitorar_em_tempo_real(obter_dados_cpu, exibir_cpu)
            
        elif opcao == '2':
            monitorar_em_tempo_real(obter_dados_memoria, exibir_memoria)
            
        elif opcao == '3':
            monitorar_em_tempo_real(obter_dados_energia, exibir_energia)
            
        elif opcao == '4':
            # a lista completa pode "piscar" na tela se for muito longa
            monitorar_em_tempo_real(listar_processos, exibir_lista_processos)
            
        elif opcao == '5':
            entrada_pid = input("Digite o número do PID do processo: ")
            try:
                pid_int = int(entrada_pid)
                monitorar_em_tempo_real(lambda: detalhar_processo(pid_int), exibir_detalhes_processo)
            except ValueError:
                print("\n[!] Erro de Entrada: O PID deve ser composto apenas por números inteiros.")
                time.sleep(2)
                
        elif opcao == '6':
            monitorar_em_tempo_real(obter_dados_sistema, exibir_sistema)
            
        elif opcao == '7':
            monitorar_em_tempo_real(obter_dados_disco, exibir_disco)
            
        elif opcao == '8':
            monitorar_em_tempo_real(obter_dados_rede, exibir_rede)
            
        elif opcao == '9':
            monitorar_em_tempo_real(obter_top_processos_memoria, exibir_top_processos_memoria)
            
        elif opcao == '10':
            monitorar_em_tempo_real(obter_top_processos_cpu, exibir_top_processos_cpu)
            
        elif opcao == '0':
            print("\nEncerrando a ferramenta de diagnóstico. Até logo!")
            break
            
        else:
            print("\n[!] Opção inválida. Por favor, escolha um número de 0 a 10.")
            time.sleep(1)

if __name__ == "__main__":
    main()