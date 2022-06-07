import sys


class Q02475:
    def solution(self):
        numbers = [int(sys.stdin.readline().strip()) for _ in range(10)]
        remainders = list(map(lambda x: x % 42, numbers))
        print(len(set(remainders)))
