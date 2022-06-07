class Q01436:
    def solution(self):
        n = int(input())
        start = 666
        while n != 0:
            if '666' in str(start):
                n -= 1
            if n == 0:
                break
            start += 1
        print(start)
