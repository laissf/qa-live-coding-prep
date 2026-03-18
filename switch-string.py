#switch the order of a string without using a built-in function
# Questions:
# - strings with spaces are allowed?
# - upper and lower cases?

# Tests:
# - happy path "string"
# - upper case "String"
# - empty string " "
# - string with space "little kid"
# - string with - "twenty-two"

#pythons strings are imutabel, so each concatenation inside the loop creates a new string and copies all the previous content
def reverseString (stringOriginal):
    stringReverse = ""
    for n in range (len(stringOriginal)):
        position = len(stringOriginal)-1-n
        stringReverse += stringOriginal[position]
    return stringReverse

stringOriginal = "string"
print(reverseString(stringOriginal))