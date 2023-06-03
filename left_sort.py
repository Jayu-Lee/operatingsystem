W = int(input())
words = input().split()

def please(a, words):
    n = len(words)
    b = [[float('inf')] * n for _ in range(n)]
    for i in range(n):
        b[i][i] = a - len(words[i])
        for j in range(i+1, n):
            b[i][j] = b[i][j-1] - len(words[j]) - 1

    penalties = [0] + [float('inf')] * n
    c = [0] * (n+1)

    for j in range(1, n+1):
        for i in range(j, 0, -1):
            if b[i-1][j-1] >= 0:
                penalty = b[i-1][j-1]**3 + penalties[i-1]
            if penalty < penalties[j]:
                penalties[j] = penalty
                c[j] = i-1
    return penalties[-1]

penalty = please(W, words)
print(penalty)
    
                
