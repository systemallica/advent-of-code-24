def main():
    with open("day_1/input.txt", "r") as file:
        list_1 = []
        list_2 = []
        # Read both columns
        for line in file.readlines():
            column_1, column_2 = line.split()
            list_1.append(int(column_1))
            list_2.append(int(column_2))

        # Sort lists
        list_1.sort()
        list_2.sort()

        # Calculate distance between column items
        distance = 0
        for value_1, value_2 in zip(list_1, list_2):
            distance += abs(value_2 - value_1)

        print(distance)


if __name__ == "__main__":
    main()
