num_element = int(input("Enter the number of elements u want to have in array as digit: "))
word_element = str(input("Enter the number of elements u want to have in array as word: "))
new_array = []
for digit in range(0,num_element):
    print("enter your int elment number ", digit+1)
    y = int(input())
    new_array.append(y)
for word in range(0,int(word_element)):
    print("enter your str elment number ", word+1)
    z = str(input())
    new_array.append(z)
print(new_array)
