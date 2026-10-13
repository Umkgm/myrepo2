import pandas as pd

f = open("scores.csv", "r",
         encoding="utf-8")
lines = f.readlines()
f.close()

print(len(lines))
print(lines[0])
print(lines[1])

header = lines[0].strip().split(",")
print(header)

first = lines[1].strip().split(",")
print(first)

cat_idx = header.index("category")
score_idx = header.index("score")

for line in lines[1:]:
    parts = line.strip().split(",")
    raw = parts[score_idx].strip()
    if raw == "":
        continue
    score = float(raw)
    print(parts[cat_idx],
          parts[score_idx])

count = 0
totals = {}
counts = {}

for line in lines[1:]:
    parts = line.strip().split(",")
    raw = parts[score_idx].strip()
    if raw == "":
        continue
    try:
        score = float(raw)
    except ValueError:
        continue
    cat = parts[cat_idx]
    if cat not in totals:
        totals[cat] = 0
        counts[cat] = 0
    totals[cat] += score
    counts[cat] += 1

    count += 1

for c in sorted(totals.keys()):
    avg = totals[c] / counts[c]
    print(c, round(avg, 2))
print(f"행의 수: {count}")