import subprocess
import os

# Configurações de Ambiente
MKV_EXTRACT_EXE = r"C:\Program Files\MKVToolNix\mkvextract.exe"
VIDEO_PATH = r"F:\ANIME\GUNDAM\GUNDAM UC\UC 0123 - GUNDAM F91\18gb\Mobile.Suit.Gundam.F91.1991.Extended.Cut.1080p.BluRay.DD+4.1.x265-Kawatare.mkv"
OUTPUT_DIR = r"F:\ANIME\GUNDAM\GUNDAM UC\UC 0123 - GUNDAM F91\18gb"


def extrair_fontes():
    # Mapeamento de tracks (ID: Nome do Arquivo)
    # 5 costuma ser ENG, 6 costuma ser JPN
    trilhas = {
        5: "matriz_ingles.ass",
        6: "matriz_japones.ass"
    }

    for track_id, filename in trilhas.items():
        output_path = os.path.join(OUTPUT_DIR, filename)

        comando = [
            MKV_EXTRACT_EXE,
            "tracks",
            VIDEO_PATH,
            f"{track_id}:{output_path}"
        ]

        print(f"--- Extraindo Track {track_id} -> {filename} ---")
        try:
            subprocess.run(comando, check=True)
            print(f"✅ Extração concluída: {output_path}\n")
        except subprocess.CalledProcessError as e:
            print(f"❌ Erro na Track {track_id}: {e}\n")


if __name__ == "__main__":
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    extrair_fontes()