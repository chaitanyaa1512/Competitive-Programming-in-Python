roman = {'I':1,'V':5,'X':10,'L':50,'C':100}

def roman_to_int(s):
   i = 0
   num = 0

   while i < len(s):
      s1=roman[s[i]]
      if (i + 1 < len(s)):
       s2 = roman[s[i + 1]]
      if (s1 >= s2):
        num=num+s1
        i+=1
      else:
        num=num+s2-s1
        i+=2
   return num
 

s = input("Enter the roman number: ")
print()
print("The Integral Value is:", end=" ")
print(roman_to_int(s))
  