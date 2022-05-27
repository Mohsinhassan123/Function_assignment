def reverse(strng):
    output = ""
    for i in strng:
        output= i + output
    return output

print(reverse("1234abcd"))
