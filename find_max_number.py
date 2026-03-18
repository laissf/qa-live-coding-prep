#find max without max() function
# Questions:
# - only int numbers?
# - negative are allowed?
# - empty lists are ok?

# tests:
# 1 - happy path
# 2 - empty list


def find_max(list_numbers):
    if not list_numbers:
        return None

    max_numb = list_numbers[0]

    for n in list_numbers:
        if n > max_numb:
            max_numb = n

    return max_numb

