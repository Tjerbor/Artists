import os.path

import pyperclip

import tools

COMPARE_IGNORE_FILE = 'compare ignore.ini'

if __name__ == '__main__':

    # print(sys.argv)
    txts = tools.get_txts()

    compare_ignore_list = []
    if os.path.isfile(COMPARE_IGNORE_FILE):
        with open(COMPARE_IGNORE_FILE, encoding="utf8") as file:
            lines = [line.rstrip() for line in file]
            lines = [line for line in lines if len(line) > 1]
            compare_ignore_list = lines

    read_txts = [tools.read_txt(txt, compare_ignore_list) for txt in txts]
    txts_clipped = [txt.rsplit('.', maxsplit=1)[0] for txt in txts]

    for i in range(len(txts_clipped)):
        name = txts_clipped[i]
        line = tools.get_random_line(read_txts[i])
        if "next" in name:
            pyperclip.copy(line)
        print(name + ":")
        print(line)
        tools.write_cleaned_txts(txts[i], read_txts[i])
