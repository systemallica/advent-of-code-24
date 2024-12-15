def main():
    total_count = 0
    r = []
    with open("./day_4/input.txt", "r") as file:
        n_lines = len(file.readlines())
        file.seek(0)
        n_columns = len(file.readline().strip())
        file.seek(0)

        data = file.read().strip().split("\n")

    # Go over data
    for line in range(n_lines):
        for column in range(n_columns):
            # Find every letter A
            if data[line][column] == "A":
                if is_within_bounds(column, line, n_columns, n_lines):
                    corners = [
                        data[line + 1][column + 1],
                        data[line + 1][column - 1],
                        data[line - 1][column - 1],
                        data[line - 1][column + 1],
                    ]

                    # Check if two corners are M and two corners are S.
                    # Also check that the 2 Ms and the 2 Ss are not on the same line/column.
                    correct_words = (
                        data[line - 1][column - 1] != data[line + 1][column + 1]
                    )
                    if (
                        corners.count("M") == 2
                        and corners.count("S") == 2
                        and correct_words
                    ):
                        total_count += 1
                        r.append(corners)

    print(total_count)


def is_within_bounds(column, line, n_columns, n_lines):
    return (line - 1 >= 0 and line + 1 < n_lines) and (
        column - 1 >= 0 and column + 1 < n_columns
    )


if __name__ == "__main__":
    main()
