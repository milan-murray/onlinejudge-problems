if __name__ == '__main__':
    m = 10000000
    prime_list = [1] * m
    for i in range(2, int(10000000 ** 0.5 + 1)):
        if prime_list[i]:
            for j in range(i * i, m, i):
                prime_list[j] = 0
    prime_list[0] = 0
    prime_list[1] = 0
    while True:
        try:
            num = int(input())
            if num < 8:
                print("Impossible.")
            else:
                ans = []
                q = num // 4
                while not prime_list[q]:
                    q -= 1
                ans.append(q)
                num -= q
                if num % 2 == 0:
                    num -= 2
                    ans.append(2)
                else:
                    num -= 3
                    ans.append(3)
                for i in range(len(prime_list)):
                    if prime_list[i] & prime_list[num-i]:
                        ans.append(i)
                        ans.append(num-i)
                        break
                print(" ".join([str(i) for i in ans]))
        except:
            break

