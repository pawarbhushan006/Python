scores = [2,45,102,4,9,12,45,90,1,0,1]
sc = 0
for i in scores:
    sc = sc + i
print(f"Total Score is {sc}")

hs = scores[0]

for i in scores:
    if hs < i:
        hs = i
print(f"Highest Score is {hs}")

ms = scores[0]

for i in scores:
    if ms > i:
        ms = i
print(f"Min Score is {ms}")

# without using for loop
print("Total score sum ",sum(scores))
print("Highest score sum ",max(scores))
print("Lowest score sum ",min(scores))