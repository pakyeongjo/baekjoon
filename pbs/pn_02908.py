class Q02908:
    def solution(self):
        a, b = input().split()
        c, d = int(a[::-1]), int(b[::-1])
        print(max(c, d))
