class Q02231:
    def solution(self):
        n, start = int(input()), 1
        result = 0
        while n > start:
            if start + sum(list(map(int, str(start)))) == n:
                result = start
                break
            start += 1
        print(result)


