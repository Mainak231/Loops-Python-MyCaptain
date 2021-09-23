#Write Python code to create a function called most_frequent
#that takes a string and prints the letters in decreasing order of frequency. Use dictionaries.

str=input("Please enter a string : ")
def most_frequent(str):
    d=dict()
    for i in str:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    sorted_order=sorted(d.items(),key=lambda x:x[1],reverse=True)
    return sorted_order
print(most_frequent(str))
