def migratoryBirds(arr):
    birds = {}
    for i in arr:
        if(i in birds):
            birds[i] += 1
        else:
            birds[i] = 1
    birds_by_val = {}
    for (key,val) in birds.items():
        if val in birds_by_val:
            birds_by_val[val].append(key)
        else:
            birds_by_val[val] = [key]
    
    sorted_dict_desc = dict(sorted(birds_by_val.items(), reverse= True))
    for j in sorted_dict_desc.values():
        sorted_array = sorted(j)
        return sorted_array[0]

print(migratoryBirds([1, 4, 4, 4, 5, 3]))
print(migratoryBirds([1, 1, 2, 2, 3]))