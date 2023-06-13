import sys
import os.path


def txt_importer(path_file):
    if not os.path.isfile(path_file):
        return print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
    if not path_file.endswith(".txt"):
        return print("Formato inválido", file=sys.stderr)
    with open(path_file) as file:
        result = [line.strip() for line in file.readlines()]
        return result
