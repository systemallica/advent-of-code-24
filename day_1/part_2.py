def main():
    with open("day_1/input.txt", "r") as file:
        list_1 = []
        list_2 = []
        # Read both columns
        for line in file.readlines():
            column_1, column_2 = line.split()
            list_1.append(int(column_1))
            list_2.append(int(column_2))
        total = 0
        for item in list_1:
            count = list_2.count(item)
            total += item * count

        print(total)


if __name__ == "__main__":
    main()
