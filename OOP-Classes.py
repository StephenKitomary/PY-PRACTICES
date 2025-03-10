class MyClass:
    language = 'python'
    version = '3.6'

print("here is the attribute for language", MyClass.language)
print("here is the attribute for version", MyClass.version)
choice = input("would you like to see your Class first y/n :")
if choice == "y":
    print(MyClass.__dict__)

else:
    pass

choice = input("do you want to add a new attribute to the class (y/n)")

if choice == "y":
    attribute_name = input ("what is the name oof the attribute that you want to add? :")
    value = input("what is the value/data for the attribute that you have created?: ")
    setattr(MyClass,attribute_name,value)
    print("All set!")
    print(MyClass.__dict__) 
else:
    print("okay i wont do it sir")
    
