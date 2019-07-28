# Create a function that return the largest number in the list

def get_largest_number(item_list):
    largest_number = 0

    for number in item_list:
        if(largest_number < number):
            largest_number = number
            
    return largest_number

result = get_largest_number([1,2,85,4,5,120,1,6,99,2])
print(result) #99


