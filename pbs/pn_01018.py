import sys


class Q01018:
    def solution(self):
        n, m = map(int, sys.stdin.readline().split())
        chess_board = [sys.stdin.readline().strip() for _ in range(n)]
        mini = []

        for a in range(n - 7):
            for i in range(m - 7):
                idx1, idx2 = 0, 0
                for b in range(a, a + 8):
                    for j in range(i, i + 8):
                        if (j + b) % 2 == 0:
                            if chess_board[b][j] != 'W': idx1 += 1
                            if chess_board[b][j] != 'B': idx2 += 1
                        else:
                            if chess_board[b][j] != 'B': idx1 += 1
                            if chess_board[b][j] != 'W': idx2 += 1
                mini.append(idx1)
                mini.append(idx2)

        print(min(mini))



