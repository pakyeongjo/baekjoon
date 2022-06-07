import sys


class Q02577:
    def solution(self):
        numbers = [int(sys.stdin.readline().strip()) for _ in range(3)]
        target = 1
        for i in numbers:
            target = i * target
        counter = [0] * 10
        for i in str(target):
            counter[int(i)] += 1
        print(counter)