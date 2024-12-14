XMAS = "XMAS"
directions = [
    [0, 1],  # 1. left to right
    [0, -1],  # 2. right to left
    [1, 0],  # 3. top to bottom
    [-1, 0],  # 4. bottom to top
    [1, 1],  # 5. diagonal top-left to bottom-right
    [1, -1],  # 6. diagonal top-right to bottom-left
    [-1, -1],  # 7. diagonal bottom-right top-left
    [-1, 1],  # 8. diagonal bottom-left top-right
]  # line increment, column increment


def has_reached_direction_end_of_line(
    line: int, column: int, n_lines: int, n_columns: int, direction: list[int]
):
    if direction[0] == 1 and line >= n_lines - 1:
        # Reached right end of line
        return True
    elif direction[1] == 1 and column >= n_columns - 1:
        # Reached bottom end of column
        return True
    elif direction[0] == -1 and line <= 0:
        # Reached left end of line
        return True
    elif direction[1] == -1 and column <= 0:
        # Reached top end of column
        return True
    else:
        return False


def is_match(
    data: list[list[str]],
    line: int,
    column: int,
    direction: list[int],
    letter_index: int,
    n_lines: int,
    n_columns: int,
) -> bool:
    if (
        has_reached_direction_end_of_line(line, column, n_lines, n_columns, direction)
        and letter_index != 3
    ):
        # Reached EOL with no match
        return False

    if data[line][column] == XMAS[letter_index]:
        if letter_index == 3:
            # Found a complete match
            return True
        else:
            # This letter matches the search, check the next one in the given direction
            letter_index += 1
            line += direction[0]
            column += direction[1]
            return is_match(
                data, line, column, direction, letter_index, n_lines, n_columns
            )
    else:
        return False


def main():
    with open("day_4/input.txt", "r") as file:
        n_lines = len(file.readlines())
        file.seek(0)
        n_columns = len(file.readline().strip())
        file.seek(0)

        lines = file.read().split("\n")
        data: list[list[str]] = [list(line) for line in lines]

        total_count = 0

        # Go over the data.
        for line in range(n_lines):
            for column in range(n_columns):
                letter_index = 0
                if data[line][column] == XMAS[letter_index]:
                    # For every X, start a search in each possible direction for a match.
                    letter_index += 1
                    for direction in directions:
                        next_line_to_check = line + direction[0]
                        next_column_to_check = column + direction[1]
                        if is_match(
                            data,
                            next_line_to_check,
                            next_column_to_check,
                            direction,
                            letter_index,
                            n_lines,
                            n_columns,
                        ):
                            total_count += 1

        print(total_count)


if __name__ == "__main__":
    main()
