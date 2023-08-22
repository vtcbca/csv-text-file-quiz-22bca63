""" create "BCA.txt" file which contain information about BCA course. count and prin the total number of lines starting with ‘A’, ‘B’, and ‘C’ in "intro.txt" file."""
f1="c:\\sqlite3\\csv\\bca.txt"
f2="c:\\sqlite3\\csv\\introduction.txt"
string='bca stands for\n, bachelor of\n, computer\n , application'
count=0
with open(f1,"w")as textfile:
    data=textfile.write(string)
with open(f1,"r")as textfile:
    data=textfile.readlines()
with open(f2,"w") as txtfile:
    for i in data:
         if(i[0]=="a" or i[0]=="A" or i[0]=="b" or i[0]=="B" or i[0]=="c" or i[0]=="C"):
               count=count+1
print("total lines:",count)



   

