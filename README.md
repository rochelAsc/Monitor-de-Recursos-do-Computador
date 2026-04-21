# Monitor de Recursos do Computador

Para facilitar, o programa tem um executavel em dist -> main.exe

Basta dar duplo click para rodar

Ferramenta de diagnóstico de sistema operacional em linha de comando (CLI), desenvolvida em Python. Este projeto monitora e exibe dados essenciais do hardware e dos processos do sistema de forma organizada e em tempo real.

Para que o programa funcione corretamente, é necessário que a máquina do avaliador possua:
1. **Python instalado** (versão 3.9 ou superior).
2. O **caminho do Python configurado nas variáveis de ambiente** (para que o comando `python` e `pip` funcionem no terminal).
3. Acesso à internet para baixar a biblioteca externa obrigatória (`psutil`).

Siga este passo a passo exato para rodar a aplicação:

1.
Extraia o arquivo `.zip` deste trabalho. Abra o terminal (Prompt de Comando, PowerShell ou terminal do Linux/Mac) e navegue até a pasta raiz onde o arquivo `main.py` está localizado.

2.
O trabalho exige o uso da biblioteca `psutil`, que não vem instalada por padrão no Python. No terminal, execute o seguinte comando para instalá-la:

pip install psutil