# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/list-comprehensions/problem?isFullScreen=true
# Problem     List Comprehensions
# Difficulty  Easy
# Subdomain   Basic Data Types
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-24, 05:14 a.m.
# ──────────────────────────────────────────────────

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    list1 =  [[i,j,k] for i in range (0,x+1)
    for j in range (0,y+1)
    for k in range (0,z+1)
    
    if n != (i+j+k)]
    print (list1)
    
