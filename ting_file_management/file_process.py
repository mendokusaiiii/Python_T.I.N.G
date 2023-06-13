from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    process_exist = False
    for process in range(len(instance._data)):
        data = instance.search(process)
        if data["nome_do_arquivo"] == path_file:
            process_exist = not process_exist
            break

    if not process_exist:
        file = txt_importer(path_file)
        file_dict = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(file),
            "linhas_do_arquivo": file,
        }
        instance.enqueue(file_dict)
        return print(file_dict, file=sys.stdout)


def remove(instance):
    file = instance.dequeue()
    if file is None:
        message_error = "Não há elementos"
        print(message_error, file=sys.stdout)
    else:
        path_file = file["nome_do_arquivo"]
        message = f"Arquivo {path_file} removido com sucesso"
        print(message, file=sys.stdout)


def file_metadata(instance, position):
    try:
        process_path_file = instance.search(position)
        return print(process_path_file, file=sys.stdout)
    except IndexError:
        message_error = "Posição inválida"
        return print(message_error, file=sys.stderr)
