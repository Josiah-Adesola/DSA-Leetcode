from collections import defaultdict
def groupAnagram(strs):
    anagram_dict = defaultdict(list)
       
    for word in strs:             
        count = [0] * 26
        
        for char in word:
            count[ord(char) - ord("a")] += 1
            
        anagram_dict[tuple(count)].append(word)
        
    return anagram_dict.values()
            
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagram(strs))

print(ord("2"))
