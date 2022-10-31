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
        k=0
        return k
    if s[1]=='*':
        k=1
        return k
    if s[2]=='*':
        k=2
        return k
    if s[3]=='*':
        k=3
        return k
    if s[4]=='*':
        k=4
        return k
    else:
        k='False'
        return k
    
    return k

print(main('*ssaf'))
        