# --------------
#Code starts here

#Function to check for palindrome
def palindrome_check(num):
  num=str(num)
  return (num[::-1]==num)

#Function to find the smallest palindrome
def palindrome(num):
    while(1):
        num=num+1
        if palindrome_check(num):
            return num
        
        
#Code ends here        


# --------------
#Code starts here

#Function to find anagram of one word in another

def a_scramble(str_1,str_2):
    result=True
    for i in (str_2.lower()):
        if i not in (str_1.lower()):
            result=False
            break
        str_1=str_1.replace(i,'',1) #Removing the letters from str_1 that are already checked
    
    return (result)

#Code ends here


# --------------
#Code starts here

def check_fib(num):
    a,b = 0,1
    L = [0,1]
    c = a + b
    for i in range(2,num+1):
        L.append(c)
        a = b
        b = c
        c = a + b
    if num in L:
        return True
    else:
        return False

        



# --------------
#Code starts here
def compress(word):
    count,index,i = 0,1,0
    word = word.lower()
    new_word = ""
    while (i < len(word)):
        w = word[i]
        for j in range(i,len(word)):
            if w == word[j]:
                count += 1
            else:
                break
        new_word = new_word+w+str(count)
        i = i+count
        count=0
    print(new_word)
    return new_word



# --------------
#Code starts here

def k_distinct(string,k):
    string = string.lower()
    L = []
    for i in range(len(string)):
        if string[i] not in L:
            L.append(string[i])
        else:
            continue

    if len(L) >=k:
        return True

    else:
        return False


