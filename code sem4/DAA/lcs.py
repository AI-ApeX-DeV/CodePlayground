def lcs(s1, s2):
    m = len(s1)
    n = len(s2)
    # Initialize the table with 0s
    table = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill the table using dynamic programming
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                table[i][j] = table[i - 1][j - 1] + 1
            else:
                table[i][j] = max(table[i][j - 1], table[i - 1][j])

    # Backtrack to find the LCS
    i = m
    j = n
    lcs = ""
    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            lcs = s1[i - 1] + lcs
            i -= 1
            j -= 1
        elif table[i - 1][j] > table[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return lcs

# Example usage
s1 = "AGCAT"
s2 = "GAC"

print(lcs(s1, s2)) # Output: "GA"
