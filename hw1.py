def transpose(matrix):
    return [list(item) for item in zip(*matrix)]


def main():
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
    print(transpose(matrix))


if __name__ == '__main__':
    main()
