def avg(nums):
    return sum(nums) / len(nums)

def status(avg):
    if avg >= 17:
        return "aali"
    elif avg >= 12:
        return "ghabol"
    else:
        return "mashrot"

n = int(input("tedad dars: "))
grades = []

for i in range(n):
    g = float(input(f"nomre {i+1}: "))
    grades.append(g)

a = avg(grades)
s = status(a)

print(f"\n moadel: {a:.2f}")
print(f"vaziat:{s}")