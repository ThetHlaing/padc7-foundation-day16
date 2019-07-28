#Request a name of the file
#Read the inputted file
#display the content line by line with while loop
#save the line into list by using append function


file_path = input("Enter file path : ")
handle = open(file_path,'r')
content_by_list = list()

for line in handle:
    print("# ",line)
    content_by_list.append(line)

print("----------------")
print(content_by_list)