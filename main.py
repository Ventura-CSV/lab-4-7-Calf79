def main():
    numbers = []
    """
    ########################################
    Code Your Program here
    ########################################
    """
    lastval = False
    while True:
        Value= int(input("input Number"))
        if lastval is not False and Value <= lastval:
            numbers.append(lastval)
        else:
            lastval = True
            if Value>lastval:
             break
        lastval==Value
    ########################################
    # Do not delete the return statement
    ########################################
    print(*numbers)
    return numbers


if __name__ == '__main__':
    main()
