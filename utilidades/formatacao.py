def converter_bytes(tamanho_em_bytes: int) -> str:

    unidades = ["B", "KB", "MB", "GB", "TB"]
    tamanho = float(tamanho_em_bytes)
    indice = 0

    while indice < len(unidades) - 1 and tamanho >= 1024:
        tamanho /= 1024
        indice += 1

    return f"{tamanho:.2f} {unidades[indice]}"

def formatar_tempo(segundos: float) -> str:

    total_segundos = int(segundos)
    horas = total_segundos // 3600
    minutos = (total_segundos % 3600) // 60
    segundos_restantes = total_segundos % 60

    return f"{horas:02d}:{minutos:02d}:{segundos_restantes:02d}"