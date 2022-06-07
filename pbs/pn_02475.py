import sys


class Q02475:
    def solution(self):
        numbers = list(map(int, sys.stdin.readline().split()))
        squared = list(map(lambda x: x ** 2, numbers))
        print(sum(squared) % 10)



