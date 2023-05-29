# ## object and classes
# x = 1
# ## this will display options for the given object
# print(dir(x))
# ## with a list you can get help with options of a list
# y = [1,2,3]
# print(dir(y))
# ## example of a dictionary object
# z = {'a':1}
# print(dir(z))
 
 
## use class to create our own objects.  classes are consider the blueprint of an object 

##class example is of a medical patient we use pass at the end to act as a place holder while we continue to write the code and prevent this from crashing

class Patient(object):
    ''' Medical centre patient''' 
    ## this would be consider a global variable that would apply to all objects within this class
    status = 'patient'
    
    def __init__(self,name,age):
        
        self.name = name
        self.age = age
    
    def print_values(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Status:", self.status)

## example of assigning values now that class has been created

steve = Patient('Steven Hughes',48)
abigail = Patient('Abigail Sandwick',32)

print(steve.name,steve.age,steve.status)
print(abigail.name,abigail.age,abigail.status)

steve.print_values()
print()
abigail.print_values()
