# Lists [ ]
    my_list = [10, 20, 30, 40, 50]
    print(my_list[0]) #the output would be 10
    print(my_list[2]) #the output would be 30
    print(my_list[-1]) #The output would be 50. Using negative indexes will return values in the end of the sequence. 

    #Ranges and Splicing
    mylist = [ "apple", "banana", "cherry", "mango", "coconut"]
    
    print(mylist[2:4]) # The output will be ['cherry', 'mango'] as cherry is the second index and mano is the last index before index 4. 
    print(mylist[4:6]) #Returns ['Coconut'] as coconut is index 4. Since there are no indexes past four, only coconut is returned. 

    print(mylist[:4]) #Returns all indexes before index 4. 
    print(mylist[3:])#Returns all indexes in the list from index 3 on.

    #Adding to a list
    	#append()
    	mylist = ["apple", "banana", "cherry"]
    	mylist.append("mango") # notice append is in parenthesis not brackets. 
    	print(mylist) #returns ["apple", "banana", "cherry", "mango"]

	#insert()
	mylist = ["apple", "banana", "cherry"]
	mylist.insert(1, "orange")
	print(mylist) #returns ["apple", "orange", "banana", "cherry"]

	#extend
	thislist = ["apple", "banana", "cherry"]
	tropical = ["mango", "pineapple", "papaya"]
	thislist.extend(tropical)
	print(thislist) #returns ["apple", "banana", "cherry", "mango", "pineapple", "papaya"]

    #Removing from a list
	#remove()
	thislist = ["apple", "banana", "cherry"]
	thislist.remove("banana")
	print(thislist) #returns ["aplee", "cherry"] 
	#note if there is more than one occurrence of the value in the list, this command will only remove the first instance. 

	#pop()
	thislist = ["apple", "banana", "cherry"]
	thislist.pop(1)
	print(thislist) #returns ["apple", "cherry"]

	#del
	thislist = ["apple", "banana", "cherry"]
	del thislist[0]
	print(thislist) #returns ["banana", "cherry"]

	#Another way to remove items is to specify to change more indexes with less than indexes than supplied. 
	thislist = ["apple", "banana", "cherry"]
	thislist[1:3] = ["watermelon"]
	print(thislist) #returns ["apple", "watermelon"]. I have effectively changed index 1 from "banana" to "watermelon" and removed index 2.
