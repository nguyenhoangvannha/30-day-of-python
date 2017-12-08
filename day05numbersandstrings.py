items = ["Viet", 'Nam', 2017, 12.7 ,"Nam moi", 7];
print(items)

print(isinstance(items[3], float))
str_items = ["Abc", "JM", "ae",'aaa','bb','ED']
print(str_items)
str_items.sort()
print(str_items)
str_items.sort(key = str.lower, reverse = True)
print(str_items)
new_items = sorted(str_items, key = str.lower, reverse = True)
print(new_items)

int_items = [12, 422,124,9, 33.5, 11.4, 48.67]
print(int_items)
int_items.sort()
print(int_items)
print(sum(int_items))