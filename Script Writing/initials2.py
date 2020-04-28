def initial_of_name(c):
    word_list = c.split(" ")
    i = (len(word_list) - 1)
    new_list = []
    for w in range(0, i):  # this loop leaves last name and creates a new list.
        word = word_list[w]
        word = word[0:1].upper()  # sliced word into initial letter
        new_list.append(word)
    new_list.append(word_list[-1])  # added last name to the list before joining.
    initial = '.'.join(new_list)
    print("The initial of your name is {0}.".format(initial))
    return


name = input("Please enter your name?\n>")
initial_of_name(name)