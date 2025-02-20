def number_words_in_doc (doc_string):
    number = 0
    words = doc_string.split()
    for word in words:
        number+=1
    return number

def charakters_counts (doc_string):
    charakters = {}
    type_list = list(doc_string)
    for i in type_list:
        i = i.lower()
        if (i in charakters.keys()):
            charakters[i] += 1
        else: 
            charakters.update({i:1})
    return charakters

def list_value (dict):
    key = list(dict.keys())[0]
    return dict[key]

def sort_list (dict_list):
    list_dictionaries = []
    for i in dict_list:
        temp_dict = {}
        temp_dict.update({i: dict_list[i]})
        list_dictionaries.append(temp_dict)
    list_dictionaries.sort(key = list_value, reverse=True)
    return list_dictionaries
                   
            
    