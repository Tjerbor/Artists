import glob
import random as rd
from difflib import SequenceMatcher


def get_txts() -> list:
    return [file for file in glob.glob("*.txt")]


def read_txt(txt, ignore_list: list = None) -> list:
    with open(txt, encoding="utf8") as file:
        lines = [line.rstrip() for line in file]
        lines = [line for line in lines if len(line) > 1]
        lines = list(set(lines))
        lines = sorted(lines, key=str.casefold)

        for line_comparer in range(len(lines) - 1):
            skip = False

            if ignore_list is not None:
                for compr in ignore_list:
                    if lines[line_comparer].lower().startswith(compr.lower()):
                        skip = True
                        break

            if not skip:
                ratio = scuffed_similar(lines[line_comparer].lower(), lines[line_comparer + 1].lower())
                if ratio > 0.8:
                    print(f'Similarity found {ratio}:\n{lines[line_comparer]}\n{lines[line_comparer + 1]}\n')

        return lines


def write_cleaned_txts(txt_name, cleaned_txt):
    with open(txt_name, 'w', encoding="utf8") as f:
        for line in cleaned_txt:
            f.write(f"{line}\n")


def get_random_line(txt: list) -> str:
    return txt[rd.randint(0, len(txt) - 1)]


def similar(a: str, b: str):
    return SequenceMatcher(None, a, b).ratio()


def scuffed_similar(a: str, b: str):
    length = min(len(a), len(b))
    # length = int((len(a) + len(b)) / 2)
    if length >= 5:
        return SequenceMatcher(None, a[:length], b[:length]).ratio()
    else:
        return SequenceMatcher(None, a, b).ratio()
