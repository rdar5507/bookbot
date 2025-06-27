from stats import *
import sys

def get_book_text(fp:str):
    with open(fp) as f:
        return f.read()


def main():
    if len(sys.argv) < 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    content = get_book_text(sys.argv[1])
    wc = word_count(content)
    letter_dict = letter_count(content)
    letter_sort_dict_ls = sorted(letter_dict)
    print('============ BOOKBOT ============')
    print('----------- Word Count ----------')
    print(f'Found {wc} total words')
    print('--------- Character Count -------')
    for i in range(0,len(letter_sort_dict_ls)):
        print(str(letter_sort_dict_ls[i]['char']) +": " + str(letter_sort_dict_ls[i]['num']))
    print('============= END ===============')



main()
    
