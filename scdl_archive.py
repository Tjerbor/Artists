import sys

import tools

if __name__ == '__main__':

    match len(sys.argv):
        case 1:
            archive = 'archive.txt'
            try:
                archive_read = tools.read_txt(archive)
                tools.write_cleaned_txts(archive, archive_read)
            except:
                pass
        case 2:
            archive = sys.argv[1]
            archive_read = tools.read_txt(archive)
            tools.write_cleaned_txts(archive, archive_read)
