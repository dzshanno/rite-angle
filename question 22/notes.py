def reVal(num):
     
    if (num >= 0 and num <= 9):
        return chr(num + 48)
    else:
        return chr(num - 10 + 65)

# Function to convert a given
# decimal number to a given base
def fromDeci(base, inputNum):
     
    # Store the result
    res = ""
     
    # Repeatedly divide inputNum
    # by base and take remainder
    while (inputNum > 0):
         
        # Update res
        res += reVal(inputNum % base)
         
        # Update inputNum
        inputNum //= base
         
    # Reverse the result
    res = res[::-1]
     
    return res



for i in range(10000):
    number_of_repunit=[]
    for j in range(2,i):
        
        binary = fromDeci(j,i)
        digits = [str(x) for x in str(binary)]
        result = all(elem == digits[0] == '1' for elem in digits)
        # print(i,j,digits)
        if result:
            number_of_repunit.append(i)
            # print(number_of_repunit)
        if len(number_of_repunit) == 3:
            print (number_of_repunit)
        