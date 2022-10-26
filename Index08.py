from re import X


def main(s):
    """
    A string of length five is given. Return the index of the "*" character, return False if not present.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    k=0
    if s[0]=='*':
        k+=1

    if s[1]=='*':
        k+=1

    if s[2]=='*':
        k+=1

    if s[3]=='*':
        k+=1

    if s[4]=='*':
        k+=1
    

        return k
    
        

print(main('qwg*e'))