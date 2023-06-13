from ting_file_management.priority_queue import PriorityQueue
import pytest


def test_basic_priority_queueing():
    queue = PriorityQueue()
    files_size = [
        {"qtd_linhas": 9},
        {"qtd_linhas": 4},
        {"qtd_linhas": 2},
        {"qtd_linhas": 5},
        {"qtd_linhas": 7},
        {"qtd_linhas": 11},
        {"qtd_linhas": 3},
    ]
    for file in files_size:
        queue.enqueue(file)

    enqueue_result = queue.high_priority._data + queue.regular_priority._data
    expected_enqueue = [
        {"qtd_linhas": 4},
        {"qtd_linhas": 2},
        {"qtd_linhas": 3},
        {"qtd_linhas": 9},
        {"qtd_linhas": 5},
        {"qtd_linhas": 7},
        {"qtd_linhas": 11},
    ]
    assert enqueue_result == expected_enqueue

    for n in range(2):
        queue.dequeue()

    dequeue_result = queue.high_priority._data + queue.regular_priority._data
    expected_dequeue = [
        {"qtd_linhas": 3},
        {"qtd_linhas": 9},
        {"qtd_linhas": 5},
        {"qtd_linhas": 7},
        {"qtd_linhas": 11},
    ]
    assert dequeue_result == expected_dequeue

    file = queue.search(0)
    assert file == {"qtd_linhas": 3}

    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        queue.search(10)
