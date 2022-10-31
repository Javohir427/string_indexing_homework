def main(s):
    """
    A string of length five is given. Return the index of the "*" character, return False if not present.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    x1=s[0]
    x2=s[1]
    x3=s[2]
    x4=s[3]
    x5=s[4]
    if x1=='*':
        return 1
    if x2=='*':
        return 2
    if x3=='*':
        return 3
    if x4=='*':
        return 4
    if x5=='*':
        return 5
    else:
        return 'False'
    


print(main('go*hs'))
        