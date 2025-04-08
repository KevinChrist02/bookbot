def get_num_words(text):
    counter = 0
    words = text.split()
    for word in words:
        counter += 1
    return counter

def get_count_char(text):
    dic = {}
    for c in text:
        c = c.lower()
        if c in dic:
            dic[c] += 1
        else:
            dic[c] = 1
    return dic

def sort_on(dic):
    return dic["count"]

def sort_dic(dic):
    char_list = []

    for char, count in dic.items():
        char_list.append({"char": char, "count": count})

    char_list.sort(reverse=True, key=sort_on)

    return char_list
