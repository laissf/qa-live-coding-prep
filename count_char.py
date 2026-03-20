def count_char(string_to_count):
    dic_count = {}
    for char in string_to_count.lower():
        if char == " ":
            continue
        elif char in dic_count:
            dic_count[char]+= 1
        else:
            dic_count[char] = 1
    return dic_count