import pyperclip

import tools

if __name__ == '__main__':
    # print(sys.argv)
    txts = tools.get_txts()
    read_txts = [tools.read_txt(txt) for txt in txts]
    txts_clipped = [txt.rsplit('.', maxsplit=1)[0] for txt in txts]

    for i in range(len(txts_clipped)):
        name = txts_clipped[i]
        line = tools.get_random_line(read_txts[i])
        if "next" in name:
            pyperclip.copy(line)
        print(name + ":")
        print(line)
        tools.write_cleaned_txts(txts[i], read_txts[i])
