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

def exibir_menu() -> None:
    print("\n" + "="*40)
    print("  FERRAMENTA DE DIAGNÓSTICO DO SO  ")
    print("="*40)
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
    print("="*40)

def main() -> None:
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção numérica: ")
        
        if opcao == '1':
            dados = obter_dados_cpu()
            exibir_cpu(dados)
            
        elif opcao == '2':
            dados = obter_dados_memoria()
            exibir_memoria(dados)
            
        elif opcao == '3':
            dados = obter_dados_energia()
            exibir_energia(dados)
            
        elif opcao == '4':
            dados = listar_processos()
            exibir_lista_processos(dados)
            
        elif opcao == '5':
            entrada_pid = input("Digite o número do PID do processo: ")
            try:
                # Garante que o usuário digitou um número antes de chamar a coleta
                pid_int = int(entrada_pid)
                dados = detalhar_processo(pid_int)
                exibir_detalhes_processo(dados)
            except ValueError:
                # Captura erros de digitação (ex: letras em vez de números)
                print("\n[!] Erro de Entrada: O PID deve ser composto apenas por números inteiros.")
                
        elif opcao == '6':
            dados = obter_dados_sistema()
            exibir_sistema(dados)
            
        elif opcao == '7':
            dados = obter_dados_disco()
            exibir_disco(dados)
            
        elif opcao == '8':
            dados = obter_dados_rede()
            exibir_rede(dados)
            
        elif opcao == '9':
            dados = obter_top_processos_memoria()
            exibir_top_processos_memoria(dados)
            
        elif opcao == '10':
            dados = obter_top_processos_cpu()
            exibir_top_processos_cpu(dados)
            
        elif opcao == '0':
            print("\nEncerrando a ferramenta de diagnóstico. Até logo!")
            break
            
        else:
            print("\n[!] Opção inválida. Por favor, escolha um número de 0 a 10.")

if __name__ == "__main__":
    main()