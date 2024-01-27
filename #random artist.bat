set regular="artist to check out regularly.txt"
set next="artist to check out next.txt"
set randomizer="Artist_List_Randomizer.jar"

java -jar %randomizer% %regular% %next%
@pause