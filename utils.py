from typing import Optional, Union, Iterable, Generator, Dict, List

from functions import filter_data, map_data, unique_data, sort_data, limit_data, regexp_data
import re

FILE = 'data/apache_logs.txt'


params_dict: dict = {
    'filter': filter_data,
    'map': map_data,
    'unique': unique_data,
    'sort': sort_data,
    'limit': limit_data,
    'regex': regexp_data,
}


def read_file(filename: str) -> Generator:
    with open(filename) as file:
        for line in file:
            yield line


def query_params(cmd1: str, value1: Union[str, int], cmd2: str, value2: Union[str, int], data: Iterable[str]) -> Dict[str, List[str]]:
    if data is None:
        prepared_data = read_file(FILE)
    else:
        prepared_data = data

    result: dict = params_dict[cmd1](params=value1, data=prepared_data)
    result2: dict = params_dict[cmd2](params=value2, data=result)
    return result2
