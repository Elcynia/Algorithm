import sys
# sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
k = int(input().strip())

for i in range(k, 0, -1):
    if i == 1:
        print(f"{i} bottle of beer on the wall, {i} bottle of beer.")
        print("Take one down and pass it around, no more bottles of beer on the wall.")
        print()
    else:
        print(f"{i} bottles of beer on the wall, {i} bottles of beer.")
        next_bottle = "bottle" if i - 1 == 1 else "bottles"
        print(f"Take one down and pass it around, {i - 1} {next_bottle} of beer on the wall.")
        print()

print("No more bottles of beer on the wall, no more bottles of beer.")
if k == 1:
    print(f"Go to the store and buy some more, 1 bottle of beer on the wall.")
else:
    print(f"Go to the store and buy some more, {k} bottles of beer on the wall.")
