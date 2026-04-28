import os
from pymediainfo import MediaInfo

folder = r"F:\ANIME"
filename = "Gundam.Reconguista.in.G.Movie.IV.Love.That.Cries.Out.in.Battle.2022.1080p.BluRay.FLAC2.0.x265-Kawatare.mkv"
full_path = os.path.join(folder, filename)

def auditoria_completa():
    if not os.path.exists(full_path):
        print(f"Erro: Arquivo não localizado em: {full_path}")
        return

    tamanho_bytes = os.path.getsize(full_path)
    tamanho_gb = tamanho_bytes / (1024 ** 3)

    mi = MediaInfo.parse(full_path)

    print(f"\n{'='*80}")
    print(f"ANÁLISE DE CONTEÚDO: {filename}")
    print(f"Tamanho do arquivo: {tamanho_gb:.2f} GB")
    print(f"{'='*80}")

    for t in mi.tracks:
        if t.track_type == "Video":
            bitrate_mbps = float(t.bit_rate) / 10**6 if t.bit_rate else 0
            print(f"[VÍDEO] {t.width}x{t.height} | {bitrate_mbps:.2f} Mbps | {t.bit_depth}-bit")

        elif t.track_type == "Audio":
            print(f"[ÁUDIO ID {t.track_id}] {t.format} | {t.language} | {t.title}")

        elif t.track_type == "Text":
            if t.format in ("UTF-8", "ASS"):
                status_traducao = "PRONTO PARA EXTRAIR (Texto)"
            else:
                status_traducao = "REQUER OCR (Imagem/PGS)"

            print(f"[LEGENDA ID {t.track_id}] {t.format} | {t.language} | {t.title}")
            print(f"  -> Status Técnico: {status_traducao}")

    print(f"{'='*80}\n")

if __name__ == "__main__":
    auditoria_completa()