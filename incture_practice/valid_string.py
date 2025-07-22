s = '24680246Z'
n = len(s)
valid = True

# Check if the last character is a vowel
if s[-1] in 'AEIOUaeiou':
    valid = False
else:
    for i in range(n - 2):  # Last char is not a digit, so check till n-2
        if (int(s[i]) + int(s[i + 1])) % 2 != 0:
            valid = False
            break

if valid:
    print("valid")
else:
    print("invalid")


