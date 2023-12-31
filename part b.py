def undoom_dice(Die_A, Die_B):
    total1 = sum(Die_A)
    total2 = sum(Die_B)
    factor = total1 / total2
    a = [min(4, value) for value in Die_A]  
    b = []
    for value in Die_B:
        adjusted_value = round(value * factor)  
        adjusted_value = min(6, adjusted_value) 
        b.append(adjusted_value)
    return a, b
initial_die_faces = [1, 2, 3, 4, 5, 6]
die_a = initial_die_faces.copy() 
die_b = initial_die_faces.copy()
new_die_a, new_die_b = undoom_dice(die_a, die_b)
print("\nNew Die A:", new_die_a)
print("New Die B:", new_die_b)