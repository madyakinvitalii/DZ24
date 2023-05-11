import re
from typing import Iterable, Iterator, List, Set, Generator


def create_generator(file_name: str) -> Iterable[str]:
    """
    Функция задания генератора для построчного чтения файла
    """
    with open(file_name) as file:
        for line in file:
            yield line


def filter_proc(value: str, data: Iterable[str]) -> Iterator[str]:
    """
    Функция filter
    """
    return filter(lambda item: value in item, data)


def map_proc(value: str, data: Iterable[str]) -> Iterator[str]:
    """
    Функция map
    """
    return map(lambda item: item.split(' ')[int(value)], data)


def sort_proc(value: str, data: Iterable[str]) -> List[str]:
    """
    Функция sorted
    """
    reverse = value == 'desc'
    return sorted(data, reverse=reverse)


def unique_proc(value: str, data: Iterable[str]) -> Set[str]:
    """
    Функция unique
    """
    return set(data)


def limit_proc(value: str, data: Iterable[str]) -> List[str]:
    """
    Функция limit
    """
    return list(data)[:int(value)]


def regex_proc(value: str, data: Iterable[str]) -> Iterator[str]:
    regex = re.compile(value)
    return filter(lambda item: re.search(regex, item), data)
