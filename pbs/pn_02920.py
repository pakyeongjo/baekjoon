import sys


class Q02920:
    def solution(self):
        s = sys.stdin.readline().strip().replace(" ", "")
        if s == '12345678':
            print('ascending')
        elif s == '87654321':
            print('descending')
        else:
            print('mixed')
