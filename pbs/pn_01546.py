import sys


class Q01546:
    def solution(self):
        n = int(input())
        scores = list(map(int, sys.stdin.readline().split()))
        max_score = max(scores)
        total_score = 0
        for score in scores:
            total_score += (score/max_score) * 100
        print(total_score/n)

