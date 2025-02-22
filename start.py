def nanana_batman(n):
    """
    This function prints "nanana" n times.

 
          
    """
    result = ""

    for i in range(n):
        result += "na"
    return result + " batman!" if result else 'batman!'


    
x = nanana_batman(0)
print(x)