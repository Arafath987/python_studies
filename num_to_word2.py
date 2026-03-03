def helper(n):
    ones = [
        "",
        "One",
        "Two",
        "Three",
        "Four",
        "Five",
        "Six",
        "Seven",
        "Eight",
        "Nine",
        "Ten",
        "Eleven",
        "Twelve",
        "Thirteen",
        "Fourteen",
        "Fifteen",
        "Sixteen",
        "Seventeen",
        "Eighteen",
        "Nineteen",
    ]
    ten = [
        "",
        "",
        "Twenty",
        "Thirty",
        "Forty",
        "Fifty",
        "Sixty",
        "Seventy",
        "Eighty",
        "Ninety",
    ]
    if n == 0:
        return ""
    elif n < 20:
        return ones[n] + " "
    elif n < 100:
        return ten[n // 10] + " " + helper(n % 10)
    else:
        return ones[n // 100] + " hundred " + helper(n % 100)


def num_to_word(n):
    res = ""
    if n >= 10000000:
        res += helper(n // 10000000) + " crores "
        n = n % 10000000
    if n >= 100000:
        res += helper(n // 100000) + " lakhs "
        n = n % 100000

    if n >= 1000:
        res += helper(n // 1000) + " thousand "
        n = n % 1000
    res += helper(n)
    return res


n = 123456
print(num_to_word(n))
