set regular="D:\Daten\Dokumente\Artists\artist to check out regularly.txt"
set next="D:\Daten\Dokumente\Artists\artist to check out next.txt"
set randomizer="C:\Users\Thiemo\IdeaProjects\Music List Tools\out\artifacts\Artist_List_Randomizer.jar"

java -jar %randomizer% %regular% %next%
@pause