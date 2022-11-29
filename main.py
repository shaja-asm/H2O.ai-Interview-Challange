# Find excel corresponding column number for column name in excel

def col2num(s):
    result = 0
    for B in range(len(s)):
        result *= 26
        result += ord(s[B]) - ord('A') + 1

    return result


ip = input("Enter column name: ")

print(col2num(ip))
