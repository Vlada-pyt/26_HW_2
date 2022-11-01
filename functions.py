def filter_data(params: str, data):
    return filter(lambda x: params in x, data)


def map_data(params, data):
    column = int(params)
    return map(lambda x: x.split(' ')[column], data)


def unique_data(data, *args, **kwargs):
    return set(data)


def sort_data(params, data):
    return sorted(data, reverse=params == 'desc')


def limit_data(params, data):
    limit = int(params)
    return data[:limit]
