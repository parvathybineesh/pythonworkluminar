numbers=[1,14,5,6,7]
even_list=[]
odd_list=[]
# for n in numbers:
#     if n%2==0:
#         even_list.append(n)
# print(even_list)

for n in numbers:
    even_list.append(n) if n%2==0 else odd_list.append(n)
print(even_list)
print(odd_list)