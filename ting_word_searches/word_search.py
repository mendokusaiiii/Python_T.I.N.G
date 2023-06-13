def exists_word(word, instance):
    return report(word, instance, "simple")


def search_by_word(word, instance):
    return report(word, instance, "complete")


def report(word, instance, report_type):
    result = []
    for process in instance._data:
        lines = process["linhas_do_arquivo"]
        occurrences = process_occurrences(word, lines, report_type)

        if len(occurrences) != 0:
            result.append(
                {
                    "palavra": word,
                    "arquivo": process["nome_do_arquivo"],
                    "ocorrencias": occurrences,
                }
            )
    return result


def process_occurrences(word, lines, report_type):
    occurrences = []
    for index in range(len(lines)):
        if word in lines[index].lower():
            if report_type == "simple":
                occurrences.append({"linha": index + 1})
            else:
                occurrences.append(
                    {"linha": index + 1, "conteudo": lines[index]}
                )
    return occurrences
