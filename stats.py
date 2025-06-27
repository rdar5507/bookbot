def word_count(content):
    c = content.split()
    return len(c)

def letter_count(content):
    con = content.lower()
    letter_dict = {}
    for i in con:
        if i not in letter_dict:
            letter_dict[i] = 1
        else:
            letter_dict[i] += 1
    return letter_dict

def sorted(items):
    def sort_on(ls):
        return ls["num"]

    letter_dict_list = []
    for i in items.keys():
        if not i.isalpha():
            continue
        temp_dict = {'char':i, 'num':items[i]}
        letter_dict_list.append(temp_dict)
    letter_dict_list.sort(reverse = True, key = sort_on)
    return letter_dict_list

    
    
