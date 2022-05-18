my_list = list('ABcdEfghI')

i = 0  # indentare necorespunzatoare
while i <= len(my_list) - 1:  # index out of range
    if my_list[i] >= 'A' and 'Z' >= my_list[i]:  # A si Z trebuiau incluse
        print(my_list[i])
    i += 1

# break - nu face parte din while
