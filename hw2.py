def key_params(**kwargs):
    return {value if value.__hash__ and value is not None else str(value): key for key, value in kwargs.items()}


def main():
    params = key_params(a=None, b='', c=[], d={})
    print(params)


if __name__ == "__main__":
    main()
