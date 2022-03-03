# Arrays

A = {1, 2, 3, 4}
B = {2, 3, 5, 6}
C = {3, 4, 6, 7}

print(A | B) # The | symbol is to join the two arrays.
print(A & B) # The & symbol is to return the intersecction between the two arrays
print(A - B) # This returns the difference between the arrays. All the elements that are in A, but not in B.
print(B - A) # This the previous operation but in reverse order. 
print(A ^ B) # This returns the "symmetrical diference" which is (A-B)|(B-A), elements that are in both arrays are excluded.
