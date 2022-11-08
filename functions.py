import re
from typing import Union, Generator, List, Iterable


def filter_data(params: str, data: Union[Generator, List[str]]):
    return list(filter(lambda x: params in x, data))


def map_data(params: str, data: Iterable[str]):
    column = int(params)
    return list(map(lambda x: x.split(' ')[column], data))


def unique_data(data: Iterable[str], *args, **kwargs):
    return set(data)


def sort_data(params: str, data: Iterable[str]):
    return sorted(data, reverse=params == 'desc')


def limit_data(params: str, data: Iterable[str]):
    limit = int(params)
    data = list(data)
    return data[:limit]

def regexp_data(params: str, data: Iterable[str]):
    data_str = list(data)
    result = []
    for line in data_str:
        if re.findall(params, line):
            result.append(line)
    return result


#a = read_file("data/apache_logs.txt")
#print(regexp_data("images\/\w{1,100}\.png", a))