'''
perm = list('ghadbicefj')

# Find the rightmost element that is smaller than the element to its right
i = len(perm) - 2
while i >= 0 and perm[i] >= perm[i+1]:
    i -= 1

# If there is no such element, then the permutation is already the smallest
if i == -1:
    print(''.join(perm))
else:
    # Find the smallest element to the right of i that is greater than perm[i]
    j = i + 1
    while j < len(perm) and perm[j] < perm[i]:
        j += 1
    j -= 1
    
    # Swap perm[i] and perm[j]
    perm[i], perm[j] = perm[j], perm[i]
    
    # Reverse the sequence to the right of i
    perm[i+1:] = reversed(perm[i+1:])
    
    # Print the previous permutation
    print(''.join(perm))
'''

def previous_permutation(s):
    for i in range(len(s) - 2, -1, -1):
        if s[i] > s[i + 1]:
            for k in range(len(s) - 1, i, -1):
                if s[i] > s[k]:
                    return s[:i] + s[k] + s[-1:k:-1] + s[i] + s[k-1:i:-1]

s = "ghadbicefj"
p = previous_permutation(s)
print(p)  # ghadbfjiec
