import sys


class Q10818:
    def solution(self):
        n = input()
        numbers = list(map(int, sys.stdin.readline().split()))
        print(max(numbers), min(numbers))

