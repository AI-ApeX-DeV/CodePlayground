# i will give input as 1110011 for the input string and 1011 for the divisor give me the code for crc function
def crc(number,divisor):
    n=len(divisor)
    number=number+"0"*(n-1)
    number=list(number)
    divisor=list(divisor)
    for i in range(len(number)-n+1):
        if number[i]=="1":
            for j in range(n):
                number[i+j]=str(int(number[i+j])^int(divisor[j]))
    return "".join(number[-n+1:])

number=input("Enter the number: ")
divisor=input("Enter the divisor: ")
print("The code is: ",crc(number,divisor))

# now the above code in appended with the number and sent to the reciever and reciever will again apply the crc function 

num=number+crc(number,divisor)
print("The number sent is: ",num)


def crc_check(num,divisor):
    n=len(divisor)
    num=list(num)
    divisor=list(divisor)
    for i in range(len(num)-n+1):
        if num[i]=="1":
            for j in range(n):
                num[i+j]=str(int(num[i+j])^int(divisor[j]))
    return "".join(num[-n+1:])
print("The remainder is: ",crc_check(num,divisor))



