list1=["chetan","rajesh","sunil","pawan","sushant"]
list2=["lohar","kumar","chodhary","nagarchi","singh rajput"]
list3=list(zip(list1,list2))
for name,cast in list3:
    print(name,cast)