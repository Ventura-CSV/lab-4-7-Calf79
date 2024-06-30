def main():
    numbers = []
    """
    ########################################
    Code Your Program here
    ########################################
    """
    lastval = None  
    while True:
            Value=int(input("Enter a number: "))
            if lastval is None or Value<=lastval:
                numbers.append(Value)
            else:
                break
            lastval=Value
    ########################################
    # Do not delete the return statement
    ########################################
    print(*numbers)
    return numbers


if __name__ == '__main__':
    main()
