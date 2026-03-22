def concat_dicts(*dicts):
    """Concatenate multiple dictionaries into a new one and return it."""
    result = {}
    for d in dicts:
        result.update(d)
    return result


if __name__ == '__main__':
    dic1 = {1: 10, 2: 20}
    dic2 = {3: 30, 4: 40}
    dic3 = {5: 50, 6: 60}

    # Method 1: using helper function
    merged = concat_dicts(dic1, dic2, dic3)
    print("Merged (helper):", merged)

    # Method 2: using unpacking (Python 3.5+)
    merged_unpack = {**dic1, **dic2, **dic3}
    print("Merged (unpacking):", merged_unpack)
