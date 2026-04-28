import re
from deep_translator import GoogleTranslator

# Configurações
INPUT_FILE = r"F:\ANIME\GUNDAM\GUNDAM UC\UC 0123 - GUNDAM F91\18gb\legenda_track_5.srt"
OUTPUT_FILE = r"F:\ANIME\GUNDAM\GUNDAM UC\UC 0123 - GUNDAM F91\18gb\legenda_ptbr.ass"


def traduzir_ass():
    translator = GoogleTranslator(source='en', target='pt')

    with open(INPUT_FILE, 'r', encoding='utf-8') as f:
        linhas = f.readlines()

    print(f"Iniciando tradução de {len(linhas)} linhas...")
    linhas_traduzidas = []

    for i, linha in enumerate(linhas):
        # O formato ASS guarda os diálogos em linhas que começam com "Dialogue:"
        if linha.startswith("Dialogue:"):
            # Dividimos a linha para pegar apenas o texto final (após a 9ª vírgula)
            partes = linha.split(',', 9)
            if len(partes) > 9:
                texto_original = partes[9].strip()

                # Tradução (mantendo tags de estilo como {\k...} se houver)
                if texto_original:
                    try:
                        traducao = translator.translate(texto_original)
                        partes[9] = traducao + "\n"
                        linha = ",".join(partes)
                        if i % 10 == 0: print(f"Traduzidas {i} linhas...")
                    except Exception as e:
                        print(f"Erro na linha {i}: {e}")

        linhas_traduzidas.append(linha)

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.writelines(linhas_traduzidas)

    print(f"\n✅ Concluído! Legenda traduzida salva em: {OUTPUT_FILE}")


if __name__ == "__main__":
    traduzir_ass()
