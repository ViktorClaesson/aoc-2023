from pathlib import Path


def parse_line(line: str) -> int:
    first_digit = next(c for c in line if c.isnumeric())
    second_digit = next(c for c in reversed(line) if c.isnumeric())
    return int(first_digit + second_digit)


def main():
    input_path = Path(__file__).parents[0] / "input.txt"
    with input_path.open() as f:
        lines = f.read().splitlines()
    print(sum(map(parse_line, lines)))


if __name__ == "__main__":
    main()
