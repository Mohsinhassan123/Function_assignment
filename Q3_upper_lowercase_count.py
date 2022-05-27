def ul_count(strng):
    uppercase = 0
    lowercase = 0
    for i in strng:
        if i.isupper():
            uppercase += 1
        elif i.islower():
            lowercase += 1
    print("No. of Upper case characters : ",uppercase)
    print("No. of Lower case Characters : ",lowercase)

ul_count('The quick Brow Fox')

