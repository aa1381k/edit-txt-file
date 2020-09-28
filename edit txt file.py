file = open("c:\\users\ALI\desktop\Test.txt","r")
try:   
    change_line = (int(input("select your line: "))-1)
    change_word = input("enter your word to be change: ")
except:
    print("please enter number!")
file2 = file.readlines()
file2 [change_line] = (change_word+ "\n")
file = open("c:\\users\ALI\desktop\Test.txt","w")
file.writelines (file2)
file.close()