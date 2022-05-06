class Q11720:
    def solution(self):
        n = int(input())
        str_numbers = input()

        numbers_list = [int(n) for n in list(str_numbers)]
        print(sum(numbers_list))
