# amobin19 09/09/2020

rev_bits = []


def toBinary(x):
    if x == 0:
        rev_bits.append(0)  # if 0 then include value in list
        rev_bits.reverse()  # reverse the list to have in binary form
        rev_bits.pop(0)  # remove additional 0 in the beginning

    else:
        var = x // 2  # get the quotient
        rem = x % 2  # get the remainder
        rev_bits.append(rem)  # add remainder to list
        toBinary(var)  # do the same for next quotient value

    return rev_bits


def main():
    decimal = int(input("Decimal value: "))  # take decimal input
    new_list = toBinary(decimal)  # list to convert to str
    for i in range(0, len(new_list)):  # loop through  each value
        new_list[i] = str(new_list[i])  # convert each value to str
    joined_list = ''.join(new_list)  # join list together
    print("Binary value: " + joined_list)  # output binary value


if __name__ == '__main__':
    main()
