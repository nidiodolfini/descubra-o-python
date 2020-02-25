word = input() #taking a string from user & storing into variable.
li = list(word) #converting the string into list & storing into variable.
ln = len(li) #storing the length of the list into a variable.
revStr = "" #defining an empty variable (which will be updated & will be final result to check palindrome).
i = ln - 1 #value of i will be used in loop.

while i >= 0: #here logic is to start from right to left from the list named "li". That means going from last to first index of the list till the index value is "0" of the "li" list.
    revStr = revStr + li[i] #concatenating & updating the "revStr" defined variable.
    i = i - 1 #decreasing the value of i to reach from the last index to first index.
word = word.lower() #converting value into lowercase string.
revStr = revStr.lower() #converting the final output into lowercase string to avoid case sensitive issue.

if word == revStr: #the two string is same or not?
    print('Palindrome') #if same.
else:
    print('Not palindrome') #if not same.