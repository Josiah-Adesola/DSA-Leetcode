def isAnagram(s,t):
    if len(s) != len(t):
        return False
    else:
        s = sorted(s)
        t = sorted(t)
        return  s == t

s = "anagram"
t = "nagaram"


print(isAnagram(s,t))