'''
Q1 lareget substring palindrom
'''

s = "babad"


def expan_from_center(left,right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    
    return s[left + 1:right]


largest = s[0]

for i in range(len(s) - 1):
    odd = expan_from_center(i,i)

    even  = expan_from_center(i,i+ 1)
    
    if len(odd) > len(largest):
        largest = odd
    if len(even) > len(largest):
        largest = even


'''
tc = O(n^2)
sc = O(1)
'''

print(largest)