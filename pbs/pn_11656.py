class Q11656:
    def solution(self):
        s = input()
        suffix = []
        for index in range(len(s)):
            suffix.append(s[index:])
        for item in sorted(suffix):
            print(item)
