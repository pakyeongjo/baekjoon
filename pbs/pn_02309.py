import sys


class Q02309:
    def solution(self):
        heights = [int(sys.stdin.readline().strip()) for _ in range(9)]
        diff = sum(heights) - 100
        heights.sort()
        fake = self.iter(diff, heights)

        for index in range(len(heights)):
            if index not in fake:
                print(heights[index])

    def iter(self, diff, array):
        for x in range(len(array)):
            for y in range(x + 1, len(array)):
                if array[x] + array[y] == diff:
                    return x, y
