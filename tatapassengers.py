def max_passengers(mat):
    n = len(mat)
    NEG = -10**9

    # dp[(r1, c1, r2)] = maximum passengers
    # c2 can be calculated from r1 + c1 = r2 + c2
    dp = {}

    def solve(r1, c1, r2):

        # Calculate position of second path
        c2 = r1 + c1 - r2

        # Out of bounds
        if r1 >= n or c1 >= n or r2 >= n or c2 >= n:
            return NEG

        # Obstruction
        if mat[r1][c1] == -1 or mat[r2][c2] == -1:
            return NEG

        # Reached destination
        if r1 == n - 1 and c1 == n - 1:
            return mat[r1][c1]

        # Already calculated
        key = (r1, c1, r2)

        if key in dp:
            return dp[key]

        # Collect passengers
        if r1 == r2 and c1 == c2:
            # Same cell -> count passenger only once
            current = mat[r1][c1]
        else:
            current = mat[r1][c1] + mat[r2][c2]

        # Four possible movements
        # 1. Both move down
        option1 = solve(r1 + 1, c1, r2 + 1)

        # 2. First moves right, second moves down
        option2 = solve(r1, c1 + 1, r2 + 1)

        # 3. First moves down, second moves right
        option3 = solve(r1 + 1, c1, r2)

        # 4. Both move right
        option4 = solve(r1, c1 + 1, r2)

        best = max(option1, option2, option3, option4)

        dp[key] = current + best

        return dp[key]

    answer = solve(0, 0, 0)

    if answer < 0:
        return 0

    return answer


# Input
n = int(input())
m = int(input())

mat = []

for i in range(n):
    row = list(map(int, input().split()))
    mat.append(row)

print(max_passengers(mat))