import os
from tkinter.filedialog import askdirectory

caminho = askdirectory(title="Selecione a pasta com os arquivos.")

lista_arquivo = os.listdir(caminho)

# Nome das pastas e respectivos formatos de arquivos
locais = {
    "Imagens": [".png", ".jpg", ".jpeg"],
    "Planilhas": [".xlsx"],
    "PDFs": [".pdf"],
    "Documentos": [".docx"],
    "Blocos de Notas": [".txt"],
    "CSVs": [".csv"],
}

def organizar_arquivos(caminho):
    for arquivo in lista_arquivo:
        nome, extensao = os.path.splitext(f"{caminho}/{arquivo}")
        for pasta in locais:
            if extensao in locais[pasta]:
                if not os.path.exists(f"{caminho}/{pasta}"):
                    os.mkdir(f"{caminho}/{pasta}")
                os.rename(f"{caminho}/{arquivo}", f"{caminho}/{pasta}/{arquivo}")

organizar_arquivos(caminho)