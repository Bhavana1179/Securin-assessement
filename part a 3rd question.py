Faces = [1, 2, 3, 4, 5, 6]
Combinations = len(Faces) * len(Faces)
print("\nProbability of Sums:")
for sum_value in range(2, 13): 
    count = 0
    for i in Faces:
        for j in Faces:
            if i + j == sum_value:
                count += 1
    probability = count / Combinations
    print(f"P(Sum = {sum_value}): {count}/{Combinations} = {probability:.2f}")