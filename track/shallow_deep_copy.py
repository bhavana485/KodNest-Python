original = [[10,20] , [30,40]]
copy = original 
copy[0][0] = 100

print(copy)
print(original)


#shallow copy 
original = [[10, 20] , [30, 40]]
copy = [original.copy()]
copy[0][0] = 100
print(copy)
print(original)

#deep copy 
import copy
original = [[10, 20] , [30, 40]]
copy_list = copy.deepcopy(original)
copy_list[0][0] = 100
print(original)
print(copy_list)
