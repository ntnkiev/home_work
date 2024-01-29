def num_couner(text):
    char_list = list(text)
    char_dict = {}
    for n in char_list:
        if n in char_dict.keys():
            char_dict[n] += 1
        else:
            char_dict.update({n : 1})
    return char_dict

fh = open('Readme.txt', 'r')
all_file = fh.read()
text = num_couner(all_file)
num1 = dict(sorted(text.items()))
for key, value in num1.items():
    print(f"{key} - {value}")
fh.close()