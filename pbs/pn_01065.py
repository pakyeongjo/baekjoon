class Q01065:
    def solution(self):
        n = int(input())
        count = 0
        for i in range(1, n+1):
            if i < 100:
                count += 1
                continue
            else:
                if int(str(i)[0]) + int(str(i)[2]) == int(str(i)[1]) * 2:
                    count += 1
        print(count)


