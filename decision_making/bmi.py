height_incm=165
weight_inkg=75
height_inm=height_incm/100
bmi=weight_inkg//height_inm**2
print(bmi)

if(bmi<=19):
    print("under weight")
elif(bmi<=25):
    print("normal")
elif(bmi<=30):
    print("obesity")

#bmi <19
#bmi 19-25 normal weight
#bmi 25-30 over weight
# >30 obesity

