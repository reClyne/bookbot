import sys
from stats import wordcount
from stats import letter_count
from stats import sort_dict


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents



def main():
    sText = get_book_text("books/frankenstein.txt")
    num_words = wordcount(sText)
    # print( num_words, "words found in the document")
    s_list = sort_dict(letter_count(sText))
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print("Found", num_words, "total words")
    print("--------- Character Count -------")
    for item in s_list:
        str = item["char"]
        n = item["num"]
        if str.isalpha() == True:
            print(str,":", " ", n, sep="")
    print("============= END ===============")

    print(sys.argv)

main()
    