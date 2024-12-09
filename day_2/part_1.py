def main():
    valid_report_count = 0
    with open("day_2/input.txt", "r") as file:
        for report in file.readlines():
            levels = report.split()
            direction = None
            is_valid_report = True

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
                        is_valid_report = False
                        continue

            if is_valid_report:
                valid_report_count += 1

    print(valid_report_count)


if __name__ == "__main__":
    main()
