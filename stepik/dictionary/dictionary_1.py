def update_dictionary(d, key, value):
    if key in d:
        list_to_addition = d[key]
        list_to_addition.append(value)
    if key not in d:
        if 2*key in d:
            list_to_addition = d[2*key]
            list_to_addition.append(value)
        if 2*key not in d:
            d[2*key] = [value]
    return d


if __name__ == '__main__':
    print(d()