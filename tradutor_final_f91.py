import re
import os
import sys
import time
import subprocess
from deep_translator import GoogleTranslator

# Configurações de Path
MKV_EXTRACT = r"C:\Program Files\MKVToolNix\mkvextract.exe"
VIDEO = r"F:\ANIME\GUNDAM\GUNDAM UC\UC 0123 - GUNDAM F91\18gb\Mobile.Suit.Gundam.F91.1991.Extended.Cut.1080p.BluRay.DD+4.1.x265-Kawatare.mkv"
MATRIZ_ENG = r"F:\ANIME\GUNDAM\GUNDAM UC\UC 0123 - GUNDAM F91\18gb\matriz_full_eng.ass"
SAIDA_PT = r"F:\ANIME\GUNDAM\GUNDAM UC\UC 0123 - GUNDAM F91\18gb\legenda_final_ptbr.ass"


def print_progress(current, total, start_time):
    percent = (current / total) * 100
    bar_length = 30
    done = int(percent / 100 * bar_length)
    bar = "█" * done + "-" * (bar_length - done)

    elapsed = time.time() - start_time
    # Estimativa de tempo restante (ETA)
    eta = (elapsed / current) * (total - current) if current > 0 else 0

    # Cores: Azul para barra, Amarelo para números, Verde para OK
    sys.stdout.write(f"\r\033[94m[{bar}] \033[93m{percent:3.1f}% \033[0m| L: {current}/{total} | ETA: {eta:.0f}s  ")
    sys.stdout.flush()


def processar():
    if not os.path.exists(MATRIZ_ENG):
        print("\033[96m--- Extraindo Track 4 (Full Script) ---\033[0m")
        subprocess.run([MKV_EXTRACT, "tracks", VIDEO, f"4:{MATRIZ_ENG}"], check=True)

    translator = GoogleTranslator(source='en', target='pt')
    with open(MATRIZ_ENG, 'r', encoding='utf-8') as f:
        linhas = f.readlines()

    total_linhas = len(linhas)
    print(f"\n\033[95mIniciando Tradução IA: {total_linhas} linhas detectadas\033[0m")

    start_time = time.time()
    novas_linhas = []

    for i, linha in enumerate(linhas):
        if linha.startswith("Dialogue:"):
            partes = linha.split(',', 9)
            if len(partes) > 9:
                texto = partes[9]
                tags = re.findall(r'\{.*?\}', texto)
                texto_limpo = re.sub(r'\{.*?\}', ' [[T]] ', texto)

                try:
                    if texto_limpo.strip() and texto_limpo.strip() != "[[T]]":
                        traducao = translator.translate(texto_limpo)
                        for t in tags:
                            traducao = traducao.replace('[[T]]', t, 1)
                        partes[9] = traducao + "\n"
                        linha = ",".join(partes)
                except:
                    pass

        novas_linhas.append(linha)

        # Atualiza o console a cada linha processada
        print_progress(i + 1, total_linhas, start_time)

    with open(SAIDA_PT, 'w', encoding='utf-8') as f:
        f.writelines(novas_linhas)

    print(f"\n\n\033[92m✅ Tradução Finalizada com Sucesso! [Tempo Total: {time.time() - start_time:.1f}s]\033[0m")


if __name__ == "__main__":
    # Limpa o console antes de começar para o Dashboard ficar no topo
    os.system('cls' if os.name == 'nt' else 'clear')
    processar()