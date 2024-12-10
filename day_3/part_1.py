import re


def main():
    with open("day_3/input.txt", "r") as file:
        total = 0
        text = file.read()
        matches = re.findall(r"mul\(\d{1,3},\d{1,3}\)", text)
        for match in matches:
            numbers = re.findall(r"\d{1,3}", match)
            result = int(numbers[0]) * int(numbers[1])
            total += result

    print(total)


if __name__ == "__main__":
    main()
