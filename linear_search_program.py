


def linear_search(args):
    print(args)
    list_search_range,found,count,float_value, delta = args
    max_delta = 0.02
    min_delta = 0.000000000001
    if((float_value == False or float_value == None or float_value == "") and (delta == None or delta == "" or delta == 0)):
        if(count==1):
            type_mismatch = False
            for i in range(len(list_search_range)):
                if(type(list_search_range[i])!=type(found)):
                    print("Type Mismatch")
                    type_mismatch = True
                if (list_search_range[i]==found):
                    return i
            if(type_mismatch==True):
                return -1
            else:
                return -100
        counted = 0
        index = []
        if(count>1):
            type_mismatch = False
            for i in range(len(list_search_range)):
                if(type(list_search_range[i])!=type(found)):
                    print("Type Mismatch")
                    type_mismatch = True
                    return -1
                if(list_search_range[i]==found):
                    counted += 1
                    index.append(i)
                    if(counted>=count):
                        return index
            if(counted==0 or counted<count):
                if(type_mismatch==True):
                    return -1
                else:
                    print("Insufficient Count:",counted)
                    return -100
    elif(float_value == True):
        if(delta == None or delta == ""):
            print("Please provide delta offset")
            return -1
        elif(delta > max_delta):
            print("delta is too big")
            return -1
        elif(delta < min_delta):
            print("delta is too small")
            return -1
        else:
            if(count==1):
                type_mismatch = False
                for i in range(len(list_search_range)):
                    if(type(list_search_range[i])!=type(found)):
                        print("Type Mismatch")
                        type_mismatch = True
                        return -1
                    if (abs(list_search_range[i]-found)<delta):
                        return i
                if(type_mismatch==True):
                    return -1
                else:
                    return -100
            counted = 0
            index = []
            if(count>1):
                type_mismatch = False
                for i in range(len(list_search_range)):
                    if(type(list_search_range[i])!=type(found)):
                        print("Type Mismatch")
                        type_mismatch = True
                        return -1
                    if(abs(list_search_range[i]-found)<delta):
                        counted += 1
                        index.append(i)
                        if(counted>=count):
                            return index
                if(counted==0 or counted<count):
                    if(type_mismatch==True):
                        return -1
                    else:
                        print("Insufficient Count:",counted)
                        return -100
    elif(float_value == "undefined" or float_value == "undef"):
        print("float value needs to be specified")
        return -1
    elif(delta%1 < min_delta):
        print("Delta has to be a small decimal value")
        return -1
def linear_search_args(args_list):
    args_defined = []
    for i in range(len(args_list)):
        args_defined.append(args_list[i])
    count = 0
    float_value = False
    delta = 0
    if(len(args_list)<2):
        print("args_list does not have enough parameters")
        return -1
    elif(len(args_list)==2):
        count = 1
        if(type(args_list[0]) != list):
            print("search list type is not a list")
            return -1
        elif(type(args_list[0])==list and type(args_list[0][0])==list or type(args_list[0][0])==dict or type(args_list[0][0])==tuple):
            float_value = ""
            delta = ""
            args_defined.append(count)
            args_defined.append(float_value)
            args_defined.append(delta)
            return linear_search(args_defined)
        elif (type(args_list[0])==list and type(args_list[0][0]) == int):
            float_value = False
            delta = 0
            args_defined.append(count)
            args_defined.append(float_value)
            args_defined.append(delta)
            return linear_search(args_defined)
        elif(type(args_list[0])==list and type(args_list[0][0]) == float):
            float_value = True
            delta = 0.000001
            args_defined.append(count)
            args_defined.append(float_value)
            args_defined.append(delta)
            return linear_search(args_defined)
        elif(type(args_list[0])==list and type(args_list[0][0]) == str):
            float_value = ""
            delta = ""
            args_defined.append(count)
            args_defined.append(float_value)
            args_defined.append(delta)
            return linear_search(args_defined)
        else:
            print("List does not contain floats or integers or strings or known data structures")
            return -1
    elif(len(args_list)==3):
        if(type(args_list[0]) != list):
            print("search list type is not a list")
            return -1
        elif(type(args_list[0])==list and type(args_list[0][0])==list or type(args_list[0][0])==dict or type(args_list[0][0])==tuple):
            float_value = ""
            delta = ""
            args_defined.append(float_value)
            args_defined.append(delta)
            return linear_search(args_defined)
        elif (type(args_list[0])==list and type(args_list[0][0]) == int):
            float_value = False
            delta = 0
            args_defined.append(float_value)
            args_defined.append(delta)
            return linear_search(args_defined)
        elif(type(args_list[0])==list and type(args_list[0][0]) == float):
            float_value = True
            delta = 0.000001
            args_defined.append(float_value)
            args_defined.append(delta)
            return linear_search(args_defined)
        elif(type(args_list[0])==list and type(args_list[0][0]) == str):
            float_value = ""
            delta = ""
            args_defined.append(float_value)
            args_defined.append(delta)
            return linear_search(args_defined)
        else:
            print("List may not contain floats or integers or strings or known data structures")
            return -1
    elif(len(args_list)==4):
        if(type(args_list[0]) != list):
            print("search list type is not a list")
            return -1
        elif(type(args_list[0])==list and type(args_list[0][0])==list or type(args_list[0][0])==dict or type(args_list[0][0])==tuple):
            delta = ""
            args_defined.append(delta)
            return linear_search(args_defined)
        elif(type(args_list[0])==list and type(args_list[0][0]) == int and float_value == False or float_value == 0):
            delta = 0
            args_defined.append(delta)
            return linear_search(args_defined)
        elif(type(args_list[0])==list and type(args_list[0][0]) == float and float_value == True or float_value == 1):
            delta = 0.000001
            args_defined.append(delta)
            return linear_search(args_defined)
        elif(type(args_list[0])==list and type(float_value)==int and float_value%1 != 0 and float_value%1 != 1):
            print("float_value needs to be either boolean or integer with values 0 or 1")
            if(type(args_list[0])==list and type(args_list[0][0]) == int):
                delta = 0
                args_defined.append(delta)
                return linear_search(args_defined)
            elif(type(args_list[0])==list and type(args_list[0][0]) == float):
                delta = 0.000001
                args_defined.append(delta)
                return linear_search(args_defined)
            elif(type(args_list[0])==list and type(args_list[0][0]) != int and type(args_list[0][0]) != float):
                delta = ""
                args_defined.append(delta)
                return linear_search(args_defined)
            else:
                print("Unknown Error")
                return -1
        elif(type(args_list[0])==list and type(args_list[0][0]) == str and float_value == ""):
            delta = ""
            args_defined.append(delta)
            return linear_search(args_defined)
        elif(type(args_list[0])==list and type(args_list[0][0]) == str and float_value != ""):
            print("Unexpected float_value")
            args_defined = []
            for i in range(5):
                args_defined.append(args_list[i])
            delta = ""
            args_defined.append(delta)
            return linear_search(args_defined)
        else:
            print("Unknown Error")
            return -1
    elif(len(args_list)==5):
        return linear_search(args_list)
    elif(len(args_list)>5):
        print("Unexpected arguments")
        args_defined = []
        for i in range(5):
            args_defined.append(args_list[i])
        return linear_search(args_defined)
search = [1,2,3,5,5]
found = linear_search_args([search,5,2])
#search = [1.4,2.3,3.2,5.9,5.9]
#found = linear_search_args([search,5.9,2])
if(type(found)!=list):
    if(found == -100):
        print("Not found")
    elif(found == -1 or found == None or found == ""):
        print("Unexpected Error encountered")
    elif(type(found)==int and found >= 0 and found < len(search)):
        print("Found index in search range : ",found)
    else:
        print("Unexpected Error, Found index needs to be an integer in the range of 0 to length of string - 1")
else:
    print("Found indexes: ",found)























































    
