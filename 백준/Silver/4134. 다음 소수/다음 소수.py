# 백준 4134번
# 정수 n은 0<=n<=4*(10**9)
# n보다 크거나 같은 소수 중 가장 작은 소수를 찾는 프로그램
# n이 n**(0.5) 보다 작거나 같은 1이 아닌 약수를 가지지 않으면 소수이다.
# n이상의 소수를 구하려면 n에서 1씩 더하면서 그 제곱근 이하의 1이 아닌 약수가 없는 수를 구하면 된다.
# n이 0 또는 1 또는 2이면 2를 출력하면 된다.
# n이 3이면 3을 출력하면 된다.
# n이 4일때 제곱근이 2이고 약수가 있는지는 2부터 n의 제곱근까지 반복해야 하므로
# n이 4일때부터 제곱근이 들어간 반복문을 돌리면 된다.
Testcase = int(input())
for i in range(Testcase):
    n = int(input())
    if n == 0 or n == 1 or n == 2:
        print(2)
    elif n == 3:
        print(3)
    elif n >= 4:
        while n != 0:
            count = 0
            for i in range(2, int(n**(0.5)) + 1, 1):
                if n % i == 0:
                    n += 1
                
                    count += 1
                    break
            if count == 0:
                print(n)
                n = 0
                break