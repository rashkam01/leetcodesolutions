def longest_prefix_compare(string_list):
    pref = ""
    shortest_string = len(min(string_list, key=len))
    for i in range(shortest_string):
        for word in string_list:
            if word[i] != string_list[0][i]:
                return pref
        pref += string_list[0][i]
            


string1 = [""]
prefix = longest_prefix_compare(string1)
print(prefix)