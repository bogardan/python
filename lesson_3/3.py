x=12
y=253
z=3898

def my_func (x:int,y:int,z:int):
    my_list = [x,y,z]
    a = max(my_list)
    my_list.pop(my_list.index(max(my_list)))
    result = max(my_list)+a
    return result

print(my_func(x,y,z))