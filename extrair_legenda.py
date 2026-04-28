import subprocess
import os

# Configurações Técnicas
MKV_EXTRACT_EXE = r"C:\Program Files\MKVToolNix\mkvextract.exe"
# Caminho da sua biblioteca Gundam
VIDEO_PATH = r"F:\ANIME\GUNDAM\GUNDAM UC\UC 0123 - GUNDAM F91\18gb\Mobile.Suit.Gundam.F91.1991.Extended.Cut.1080p.BluRay.DD+4.1.x265-Kawatare.mkv"
OUTPUT_DIR = r"F:\ANIME\GUNDAM\GUNDAM UC\UC 0123 - GUNDAM F91\18gb"


def extrair_legenda(track_id):
    # Definimos o nome do arquivo de saída
    output_file = os.path.join(OUTPUT_DIR, f"legenda_track_{track_id}.srt")

    comando = [
        MKV_EXTRACT_EXE,
        "tracks",
        VIDEO_PATH,
        f"{track_id}:{output_file}"
    ]

    print(f"Executando: {' '.join(comando)}")
    try:
        # shell=False é mais seguro para evitar injeção, mas shell=True lida melhor com caminhos complexos no Windows
        subprocess.run(comando, check=True)
        print(f"\n✅ SUCESSO: Legenda extraída em {output_file}")
        return output_file
    except subprocess.CalledProcessError as e:
        print(f"\n❌ ERRO na extração: {e}")
        return None


if __name__ == "__main__":
    # Vamos tentar o ID 5, que costuma ser a primeira legenda após os áudios
    extrair_legenda(5)