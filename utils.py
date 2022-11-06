from typing import Optional

from functions import filter_data, map_data, unique_data, sort_data, limit_data

FILE = 'data/apache_logs.txt'


params_dict = {
    'filter': filter_data,
    'map': map_data,
    'unique': unique_data,
    'sort': sort_data,
    'limit': limit_data,
}


def read_file(filename):
    with open(filename) as file:
        for line in file:
            yield line


def query_params(cmd, value, data: Optional):
    if data is None:
        prepared_data = read_file(FILE)
    else:
        prepared_data = data
    result = params_dict[cmd](params=value, data=prepared_data)
    return list(result)
