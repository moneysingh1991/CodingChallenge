
# This function
#argument 1:  nested list of intger
#argument 2 : list to return
#return list
def flatten(array,returnList):
    for item in array:
        if isinstance(item,int):
            returnList.append(item)
        else:
            flatten(item,returnList)
  
    return returnList


#Testing
print(flatten([0, [ [1,2], [ 3, [ 4, [5, 6] ] ] ] ],[])) 
print(flatten([[1,2,[3]],4],[]))
print(flatten([],[]))


