list = [20,1,7,20,50]
print('minimum value in the list is', min(list))
print('max value in the list is', max(list))

# Method-2
def my_min_function(onelist):
    min_value = []
    for value in onelist:
        if not min_value:
            min_value = value
        elif value < min_value[0]:
            min_value[0] = value
    return min_value[0]

 def my_max_function(onelist):
    max_value = []
    for value in onelist:
        if not max_value:
            min_value = value
        elif value > max_value[0]:
            max_value[0] = value
    return max_value[0]
  
 print('minimum value in the list is', my_max_function(list))
 print('max value in the list is', my_min_function(list))
