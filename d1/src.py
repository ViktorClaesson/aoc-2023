import re
from pathlib import Path


def reverse_string(string: str) -> str:
    return "".join(reversed(string))


def part_1_parse_line(line: str) -> int:
    first_digit = next(c for c in line if c.isnumeric())
    second_digit = next(c for c in reversed(line) if c.isnumeric())
    return int(first_digit + second_digit)


def part_1(lines: list[str]) -> int:
    return sum(map(part_1_parse_line, lines))


def part_2_parse_line(line: str) -> int:
    numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    mapper = {
        **{number: str(index) for index, number in enumerate(numbers, start=1)},
        **{reverse_string(number): str(index) for index, number in enumerate(numbers, start=1)},
    }
    pattern = f"([0-9]|{'|'.join(numbers)})"
    pattern_reversed = f"([0-9]|{'|'.join(map(reverse_string, numbers))})"
    first_digit = re.search(pattern, line).group()
    second_digit = re.search(pattern_reversed, reverse_string(line)).group()
    return int(mapper.get(first_digit, first_digit) + mapper.get(second_digit, second_digit))


def part_2(lines: list[str]) -> int:
    return sum(map(part_2_parse_line, lines))


def main():
    input_path = Path(__file__).parents[0] / "input.txt"
    with input_path.open() as f:
        lines = f.read().splitlines()

    print("part_1:", part_1(lines))
    print("part_2:", part_2(lines))


if __name__ == "__main__":
    main()
