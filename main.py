import sys
from stats import number_words_in_doc
from stats import charakters_counts
from stats import sort_list

def get_book_text (filepath):
    f = open(filepath, "r")
    file_contents = f.read()
    f.close()
    return file_contents


def main():
    if (len(sys.argv) != 2):
        print ("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_in_string = get_book_text(sys.argv[1])
    list_count = charakters_counts(file_in_string)
    list_items  = sort_list(list_count)
    print ( "============ BOOKBOT ============")
    print (f"Analyzing book found at {sys.argv[1]}...")
    print ("----------- Word Count ----------")
    print (f"Found {number_words_in_doc(file_in_string)} total words")
    print ("--------- Character Count -------")
    for i in list_items: 
       # print(f"{list(dict.keys()[0])}: {i[list(i.keys()[0])]}")
        j = list(i)
        print(f"{j[0]}: {i[j[0]]} ")
main()