import os


def localizar_mkvtoolnix():
    caminhos_provaveis = [
        r"C:\Program Files\MKVToolNix\mkvextract.exe",
        r"C:\Program Files (x86)\MKVToolNix\mkvextract.exe",
        os.path.join(os.environ.get("LocalAppData", ""), r"Programs\MKVToolNix\mkvextract.exe"),
    ]

    print("Iniciando busca pelo executável...")
    for caminho in caminhos_provaveis:
        if os.path.exists(caminho):
            print(f"✅ ENCONTRADO: {caminho}")
            return caminho
        else:
            print(f"❌ Não está em: {caminho}")

    print("\nERRO CRÍTICO: O MKVToolNix não foi encontrado nos locais padrão.")
    print(
        "Dica: Abra o 'MKVToolNix GUI' pelo menu iniciar, clique com o botão direito no ícone e vá em 'Abrir local do arquivo'.")
    return None


if __name__ == "__main__":
    localizar_mkvtoolnix()