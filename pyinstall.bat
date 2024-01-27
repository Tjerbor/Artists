set script=artists
pyinstaller --onefile %script%.py
copy .\dist\%script%.exe .\%script%.exe

set script=scdl_archive
pyinstaller --onefile %script%.py
copy .\dist\%script%.exe .\%script%.exe

rmdir /Q /S build dist
del /f *.spec