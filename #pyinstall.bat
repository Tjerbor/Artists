set script=artists
pyinstaller --onefile %script%.py
copy .\dist\%script%.exe .\%script%.exe

Rem set script=scdl_archive
Rem pyinstaller --onefile %script%.py
Rem copy .\dist\%script%.exe .\%script%.exe

rmdir /Q /S build dist
del /f *.spec