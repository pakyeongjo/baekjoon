import sys


class Q02751:
    def solution(self):
        n = int(input())
        numbers = [int(sys.stdin.readline().strip()) for _ in range(n)]

        for item in sorted(set(numbers)):
            print(item)
