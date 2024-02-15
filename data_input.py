filename = "data_input.txt"

in_file = open(filename, "r")

for line in in_file:
    print(line)

in_file.close()
