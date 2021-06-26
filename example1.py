try:
    a =[1,2]
    print(a[1])
    c=1/1
    if c== 1:
        raise IndexError
except IndexError as e:
    print(e)
    print("please make sure the index less than the list size")
except ZeroDivisionError as z:
    print("your divider is zero which is invalid")
    exit(2)
except NameError as ne:
    print("please make sure that vars that are using are defined")
else:
    print("Hey we are good with exceptions")
finally:
    print("I am on top of all. Exceptions can't touch me")