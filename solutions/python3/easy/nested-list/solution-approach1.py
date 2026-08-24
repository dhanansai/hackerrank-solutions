# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true
# Problem     Nested Lists
# Difficulty  Easy
# Subdomain   Basic Data Types
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-25, 04:55 a.m.
# ──────────────────────────────────────────────────

if __name__ == '__main__':
    record = []
    scores = set()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        record.append([name,score])
        scores.add(score)
    
    second_score = sorted(scores)[1]
    for name, score in sorted(record):
        if score == second_score:
            print (name)
        
