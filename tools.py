import glob
import random as rd


def get_txts() -> list:
    return [file for file in glob.glob("*.txt")]


def read_txt(txt) -> list:
    with open(txt, encoding="utf8") as file:
        lines = [line.rstrip() for line in file]
        lines = [line for line in lines if len(line) > 1]
        lines = list(set(lines))
        lines = sorted(lines, key=str.casefold)
        return lines


def write_cleaned_txts(txt_name, cleaned_txt):
    with open(txt_name, 'w', encoding="utf8") as f:
        for line in cleaned_txt:
            f.write(f"{line}\n")


def get_random_line(txt: list) -> str:
    return txt[rd.randint(0, len(txt) - 1)]
