from coleta.cpu import obter_dados_cpu
from coleta.memoria import obter_dados_memoria
from coleta.energia import obter_dados_energia
from coleta.processos import listar_processos, detalhar_processo

from visao.terminal import (exibir_cpu, exibir_memoria, exibir_energia, 
                            exibir_lista_processos, exibir_detalhes_processo)

def exibir_menu() -> None:

    print("\n" + "="*35)
    print("  FERRAMENTA DE DIAGNÓSTICO DO SO  ")
    print("="*35)
    print("1. Consultar Processador (CPU)")
    print("2. Consultar Memória RAM")
    print("3. Consultar Energia/Bateria")
    print("4. Listar Processos em Execução")
    print("5. Detalhar Processo por PID")
    print("0. Sair do Programa")
    print("="*35)

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
                
        elif opcao == '0':
            print("\nEncerrando a ferramenta de diagnóstico. Até logo!")
            break
            
        else:
            print("\n[!] Opção inválida. Por favor, escolha um número de 0 a 5.")


if __name__ == "__main__":
    main()