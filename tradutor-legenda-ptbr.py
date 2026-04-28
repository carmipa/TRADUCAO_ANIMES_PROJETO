import re
from concurrent.futures import ThreadPoolExecutor
from deep_translator import GoogleTranslator
from tqdm import tqdm
from colorama import Fore, init

init(autoreset=True)


def translate_line(line, translator):
    if line.startswith('Dialogue:'):
        parts = line.split(',', 9)
        if len(parts) > 9:
            prefix = ','.join(parts[:9])
            text = parts[9].strip()
            # Proteção de Tags ASS
            tags = re.findall(r'\{.*?\}', text)
            clean_text = re.sub(r'\{.*?\}', ' [[TAG]] ', text)
            try:
                translated = translator.translate(clean_text)
                for tag in tags:
                    translated = translated.replace('[[TAG]]', tag, 1)
                return f"{prefix},{translated}\n"
            except:
                return line
    return line


def translate_ass_turbo(input_file, output_file, max_workers=20):
    translator = GoogleTranslator(source='auto', target='pt')

    with open(input_file, 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()

    print(f"{Fore.YELLOW}Iniciando tradução TURBO (Multithread) de {len(lines)} linhas no HD Mecânico...")

    # Processamento paralelo com 20 workers
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # Mapeamos a função para todas as linhas
        results = list(tqdm(executor.map(lambda l: translate_line(l, translator), lines),
                            total=len(lines),
                            desc=f"{Fore.CYAN}Traduzindo",
                            bar_format="{l_bar}{bar:30}{r_bar}",
                            colour='green'))

    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(results)

    print(f"\n{Fore.GREEN}✔ Deploy concluído com Multithreading! Arquivo: {output_file}")


if __name__ == "__main__":
    # Ajuste os caminhos absolutos para o seu drive F:
    input_f = r"F:\ANIME\GUNDAM\GUNDAM UC\UC 0123 - GUNDAM F91\18gb\legenda_final_ptbr.ass"
    output_f = r"F:\ANIME\GUNDAM\GUNDAM UC\UC 0123 - GUNDAM F91\18gb\Gundam_F91_Fidelity_PTBR.ass"
    translate_ass_turbo(input_f, output_f)