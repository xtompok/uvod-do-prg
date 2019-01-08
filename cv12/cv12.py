from operator import itemgetter
points = [{"coords":[14,48]},{"coords":[15,50]},
        ]
s = [p["coords"] for p in points]
s = [p["coords"] for p in points if p["coords"][0]>14]
print(s)

def twice(n):
    return 2*n

numbers = ["12","14","23"]
nums = list(map(int,numbers))
doubled = list(map(twice,nums))
print(nums)
print(doubled)

s2 = list(map(itemgetter('coords'),points))
s3 = list(map(lambda p:p['coords'],points))
print(s2)
print(s3)

def bignum(n):
    if n > 13:
        return True
    else:
        return False

bignums = list(filter(bignum,nums))
bignums2 = list(filter(lambda n:n>13,nums))

print(bignums)
print(bignums2)

# TODO enumerate


