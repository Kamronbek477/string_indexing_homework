






def main(s):
    """
    Given a variable s string of length five. Determine the number of digits involved in this variable.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """

    k=0
    if s[0].isdigit():
        k+=1
    if s[1].isdigit():
        k+=1
    if s[2].isdigit():
        k+=1
    if s[3].isdigit():
        k+=1
    if s[4].isdigit():
        k+=1
    return k
print(main("3oui2"))