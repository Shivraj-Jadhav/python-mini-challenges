# --------------
#Code starts here
def palindrome(num):
    num=num+1
    while True:
        num1=str(num)
        num1=num1[::-1]
        if int(num1) == num:
            return int(num1)
        else:
           num=num+1

#num=int(input())
#print(palindrome(num))



# --------------
#Code starts here
def a_scramble(str_1,str_2):
    str_1 =sorted(str_1.lower())
    str_2 =sorted(str_2.lower())
    for i in str_2:
        if i in str_1:
            str_1.remove(i)
            l=0
        else:
            return False
            break
    if l==0:
        return True




# --------------
#Code starts here
def check_fib(num):
    a=0
    b=1
    i=a
    while True:
        c=a+b
        a=b
        b=c
        i=c
        if i>=num:
            break
    if i ==num:
        return True
    else:
        return False



# --------------
#Code starts here
def compress(word):
    word=word.lower()
    count = 1
    result = word[0]
    for i in range(len(word)-1):
        if(word[i] == word[i+1]):
            count+=1
        else:
            result += str(count)
            result += word[i+1]
            count = 1
    result += str(count)        
    return result


# --------------
#Code starts here
def k_distinct(string,k):
    a_list = []
    a_list = string[:].lower()
    a_set = set(a_list)
    n = len(a_set)
    if n == k:
        return True
    else:
        return False




