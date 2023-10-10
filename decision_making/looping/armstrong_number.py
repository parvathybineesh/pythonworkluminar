number=int(input("enter number >"))

orginal=number
digit_count=len(str(number))
sum=0
while(number !=0):
    last_digit=number %10
    exponent=last_digit**digit_count
    sum=sum+exponent
    number =number//10
print("armstrong number" if sum==orginal else "not armstrong")