def square_digits(num):
    to_str = str(num)
    
    int_list   = [int(n)*int(n) for n in to_str]         ## Initialized a list of integers
    
    str_list   = [str(e) for e in int_list]              ## Converted all elements to str in a new list
    
    join_str   =  "".join(element for element in str_list)      ## Joined all elements
    
    num_int = int(join_str)                                     ## Converted it into integer
    
    return num_int
