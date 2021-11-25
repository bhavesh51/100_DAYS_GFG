print("array revere")
#input : arr[] = {1,2,3,4,5,6}
#d=2 here d is index value
#output : arr[] = {3,4,5,6,1,2}
arr = [1,2,3,4,5,6]
d = 5
temp_arr = []
main_arr = []
print(arr)
for i in range(0,d):
    temp_arr.append(arr[i])
print("temparr", temp_arr)
print("arr", arr)
for i in range(d+1,arr[-1]+1):
    main_arr.append(i)
print("main_arr",main_arr)
print(main_arr + temp_arr)