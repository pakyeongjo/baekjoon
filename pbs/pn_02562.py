class Q02562:
    def solution(self):
        top = -1
        index = 1
        for i in range(1, 10):
            n = int(input())
            if n > top:
                top, index = n, i
