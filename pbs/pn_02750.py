import sys


class Q02750:
    def solution(self):
        n = int(input())
        numbers = [int(sys.stdin.readline().strip()) for _ in range(n)]

        for item in sorted(numbers):
            print(item)
