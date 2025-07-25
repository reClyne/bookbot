import sys
from stats import wordcount
from stats import letter_count
from stats import sort_dict


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def no_book_path():
    n_list = sys.argv
    if len(n_list) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

def get_book():
    n_list = sys.argv
    return n_list[1]


def main():
    no_book_path()
    sText = get_book_text(get_book())
    num_words = wordcount(sText)
    # print( num_words, "words found in the document")
    s_list = sort_dict(letter_count(sText))
    print("============ BOOKBOT ============")
    print("Analyzing book found at ",get_book(),"...", sep="")
    print("----------- Word Count ----------")
    print("Found", num_words, "total words")
    print("--------- Character Count -------")
    for item in s_list:
        str = item["char"]
        n = item["num"]
        if str.isalpha() == True:
            print(str,":", " ", n, sep="")
    print("============= END ===============")

    #print(sys.argv)

main()
    