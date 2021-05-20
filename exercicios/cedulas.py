n=int(input())


if 0 < n < 1000:
    x = n // 100
    print('{} nota(s) de R$ 100'.format(x))
    y = n % 100
    z = y // 50
    print('{} nota(s) de R$ 50'.format(z))
    w = y % 50
    q = w // 20
    print('{} nota(s) de R$ 20'.format(q))
    u = w % 20
    i = u // 10
    print('{} nota(s) de R$ 10'.format(i))
    v = u % 10
    n = v // 5
    print('{} nota(s) de R$ 5'.format(n))
    j = v % 5
    h = j // 2
    print('{} nota(s) de R$ 2'.format(h))
    a = j % 2
    b = a // 1
    print('{} nota(s) de R$ 1'.format(b), end="")