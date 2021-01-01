def min_coins (n, index):
    denomination_list = [1, 5, 10, 25]

    quotient =int  (n / denomination_list[index])
    remainder = n % denomination_list[index]

    if remainder == 0:
        return quotient
    else:
        quotient += min_coins(remainder, index -1)

    return quotient



if __name__ == "__main__":
    print (min_coins (n,3))  # choose any amount for n in cents
