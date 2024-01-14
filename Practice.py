#Sets { } 
    # - Unordered, immutable, and unindexed.
    # - Duplicates are NOT allowed.
    # - Adding and removing indices is allowed.
# Sets Practice
    fruits = {"apple", "banana", "orange", "apple"}

    print(len(fruits) # would return 3, because duplicates are not allowed.
    print(fruits) # would return "('apple', 'banana', 'orange')", because duplicates are not allowed.

# Lists [ ] 
      # - Ordered and changeable. Duplicates are allowed.
      # - A sequenced collection of different objects such as integers, strings, and even other lists as well.
# Lists Practice
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
    mylist = ["apple", "banana", "cherry"]
    mylist[1] = "blackcurrant"
    print(thislist)
    mylist = ["apple", "blackcurrant", "banana", "cherry"]

# Tuples ( )
    # - Ordered and immutable. Duplicates are allowed. Faster for processing.
    # - Can contain different data types.
# Tuples Practice 

          
#Dictionaries { } 
    # - Used to store key-value pairs.
    # - The keys have to be immutable and unique and are often characters.
    # - Dictionaries support any data type.
#Practice
   Cars = {
      "brand": "Ford",
      "model": "Mustang",
      "year": 1964
	    "color": "red"
    }
    # --- Basic Commands
    print(Cars) #returns the above dictionary
    print(len(Cars)) # returns 4 as there are 4 sets of key-value pairs. 

    # --- Accessing broad dictionary contents
    print(Cars.values()) #prints all of the values in the dictionary
    print(Cars.keys()) #prints all of the keys in the dictionary

    # --- Accessing specific dictionary contents
    print(Cars["brand"]) #prints "Ford" as this the corresponding value for the key "brand".
    x = Cars["model"] 
    print(x) # This is another way of returning a specific key value based on the key you provided.
    
    # --- Changing values in a dictionary
    dictionary_name["key_name"] = "new_desired_value"
    #alteratively you can use
    dictionary_name.update({"key_name": "key_value"})

    # --- Adding dictionary values
    dictionary_name["new_key"] = "new_value" #adds a new key-value pair to the dict. 
    #alt
    dictionary_name.upadate{"new_key": "new_value"}) #adds a new key-value pair to the dict. 

    # --- Removing dictionary values
    dictionary_name.pop["key_name"] #removes the key-value pair from the dict. 
    #alt
    del dictionary_name["key_name"] #removes the key-value pair from the dict.

    
