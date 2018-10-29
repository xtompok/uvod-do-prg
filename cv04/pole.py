from math import sqrt

N = 100


def get_primes(N):
    """ Vrací seznam prvočísel menších rovno N """
    nums = list(range(N+1))
    prime = 2
    while prime <= N:
        if nums[prime] == None:
            prime += 1
            continue
        n = prime*2
        while n <= N:
            nums[n] = None
            n = n+prime
        prime += 1

    primes=[]
    for num in nums:
        if num != None:
            primes.append(num)

    primes = primes[2:]
    return primes


def solve_quadratic(a,b,c):
    """
    Reší kvadratickou rovnici s parametry a,b,c

    :return: Vrací (<počet řešení>,<seznam kořenů>)
    """
    D = b*b-4*a*c
    if D < 0:
        return (0,[])
    if D == 0:
        x12 = -b/2*a
        return (1,[x12,x12])
    # zde nemusí být else, protože v předchozích
    # ifech jsme z funkce vyskočili, tudíž se sem
    # dostaneme jen tehdy, když D > 0
    x1 = -b+sqrt(D)/2*a
    x2 = -b-sqrt(D)/2*a
    return (2,[x1,x2])


print(get_primes(10))
print(get_primes(100))
print(get_primes(1000))

print(solve_quadratic(1, 0, 1))
print(solve_quadratic(1, 0, -1))
print(solve_quadratic(1, 2, 1))
