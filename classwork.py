t1 = ('bennington',)
print(t1)

t2=('Bennington',2024)
print(t2)

t3 = ('Dickinson',)
print(t2+t3)

def intersect(t1, t2):
    result = ()
    for e in t1:
        if e in t2:
            result += (e,)
    return result
print(intersect((1, 'a', 2), ('b', 2, 'a')))

"""The for loop iterates through the tuple on element at a time, and assigns it to a variable e"""
"""The if loop compares if the e element is found inside the t2 touple """


def myfunction(a,b):

    sum = a+b
    sub = a-b
    prod=a*b
    div = a/b
    result= (sum,sub,prod,div)

    return result

print(myfunction(4,2))