def product(*args):
    res=1
    for n in args:
        res*=n
    return res
print(product(1,2,3,4,5))

#create a function max_word that will accept any number of parametres and return lengthy string

def max_word(*args):
    lengthy_word=max(args,key=lambda w:len(w))
    return(lengthy_word)
print(max_word("hello","goodmorning","evening"))