import sys


class Q07568:
    def solution(self):
        n = int(sys.stdin.readline())
        specs = []

        for i in range(n):
            weight, height = map(int, sys.stdin.readline().split())
            specs.append((weight, height, i))
        sorted_specs = sorted(specs, key=lambda x: x[0])
        rank = [0] * n

        for index in range(len(sorted_specs)):
            count = 1
            for item in range(index + 1, len(sorted_specs)):
                if sorted_specs[index][0] == sorted_specs[item][0]:
                    pass
                elif sorted_specs[index][1] < sorted_specs[item][1]:
                    count += 1
            rank[sorted_specs[index][2]] = count

        print(*rank)
