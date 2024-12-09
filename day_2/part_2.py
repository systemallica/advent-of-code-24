def main():
    valid_report_count = 0
    with open("day_2/input.txt", "r") as file:
        for report in file.readlines():
            levels = report.split()
            if is_valid_report(levels):
                valid_report_count += 1
            else:
                # Check if removing an element from the report makes it valid
                for i in range(len(levels)):
                    levels_copy = levels.copy()
                    levels_copy.pop(i)
                    if is_valid_report(levels_copy):
                        valid_report_count += 1
                        break

    print(valid_report_count)


def is_valid_report(levels: list[str]) -> bool:
    direction = None
    previous_level = None
    for i in range(len(levels)):
        level = int(levels[i])

        if i == 0:
            previous_level = level
        elif i == 1:
            direction = "ascending" if level > previous_level else "descending"
        if i >= 1:
            is_valid_distance = 1 <= abs(level - previous_level) <= 3
            is_valid_level_progression = (
                level > previous_level
                if direction == "ascending"
                else level < previous_level
            )
            previous_level = level
            if not (is_valid_distance and is_valid_level_progression):
                return False
    return True


if __name__ == "__main__":
    main()
