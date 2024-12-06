str1 = "Bartek"
str2 = "JhonDipPeta"


def three_letters(str):
    result = ""
    result += str[0]
    result += str[len(str) // 2]
    result += str[-1]
    return result


print(three_letters(str1))


def three_middle_letters(str):
    middle = len(str) // 2
    a = str[middle - 1]
    b = str[middle]
    c = str[middle + 1]
    result = a + b + c
    return result


print(three_middle_letters(str2))


def add_string_in_the_middle(str, str2):
    middle = len(str) // 2
    a = str[:middle]
    b = str[middle:]
    inside = str2
    result = a + inside + b
    return result


print(add_string_in_the_middle("Bartek", "abc"))
