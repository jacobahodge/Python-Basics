#Dictionaries { }
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

    
