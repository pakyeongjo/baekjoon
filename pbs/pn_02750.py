import sys


class Q05052:
    def solution(self):
        n = int(input())
        numbers = [int(sys.stdin.readline().strip()) for i in range(n)]

        for item in sorted(numbers):
            print(item)
