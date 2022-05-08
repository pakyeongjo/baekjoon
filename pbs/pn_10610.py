class Q10610:
    def solution(self):
        words = list(int(x) for x in input())

        if 0 not in words or not sum(words) % 3 == 0:
            print(-1)
        else:
            print("".join(map(str, sorted(words, reverse=True))))
