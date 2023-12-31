Faces = [1, 2, 3, 4, 5, 6]
Combinations = len(Faces) * len(Faces)
print("\nCombinations Distribution:")
for i in Faces:
    for j in Faces:
        print(f"({i}, {j})", end=" ")
        if j == Faces[-1]:
            print()