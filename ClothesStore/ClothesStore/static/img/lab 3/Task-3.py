#Task3
from collections import Counter
file1 = open("file1.txt", "w")
file1.write("Far out in the uncharted backwaters of the " +
            "unfashionable end of the western spiral arm of "+
            "the Galaxy lies a small unregarded yellow sun.")
file1.close()
file2 = open("file2.txt", "w")
file2.write("This planet has - or rather had a problem, "+
            "which was this: most of the people on it were"+
            " unhappy for pretty much of the time. ")
file2.close()
file3 = open("file3.txt", "w")
file3.write("The house stood on a slight rise just on the"+
            " edge of the village.")
file3.close()
print("\tMy Files: \n(1)file1.txt \n(2)file2.txt \n(3)file3.txt")

def counters():
    name=input("Input a file name with the extension .txt: ")
    if name=="file1.txt":
        opener=open("file1.txt")
    elif name=="file2.txt":
        opener=open("file2.txt")
    elif name=="file3.txt":
        opener=open("file3.txt")
    else:
        print("This file doesn`t exist")
    list_words=opener.read()
    print(list_words)
    counter_words=str(Counter(list_words.split()))
    new_file=open("new_file.txt","w")
    new_file.write(counter_words)
    new_file.close()
    opener.close()
    new_file=open("new_file.txt")
    all_words=new_file.read()
    print(all_words)
    new_file.close()
counters()
