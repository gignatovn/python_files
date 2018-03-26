
list=['apple','bannana','carrot','rice','orange','waffle','beer ']

for i in range(len(list)):
    if i == len(list) -2 :
        print(list[i], end=' and ')
    elif i != len(list) -1:
        print(list[i], end=', ')
    else:
        print(list[i])
