P = input("Enter your gender M/F:")
C = int(input("Enter the lunch time :"))
if P=="M" and C==2:
	print("you can have Lunch — 600–650 kcal 2 roti → 200 kcal Dal → 200 kcal Sabzi → 100 kcal Curd → 100 kcalTotal ≈ 600 kcal")
elif P=="F" and C==2:
	print("you can have Lunch — 500–650 kcal 2 roti → 200 kcal Dal → 200 kcal Sabzi → 100 kcal Curd → 100 kcalTotal ≈ 500 kcal")
elif P=="M" and C==1:
	print("you can have Lunch — 400–650 kcal 2 roti → 200 kcal Dal → 200 kcal Sabzi → 100 kcal Curd → 100 kcalTotal ≈ 400 kcal")
elif P=="F" and C==1:
	print("you can have Lunch — 300–650 kcal 2 roti → 200 kcal Dal → 200 kcal Sabzi → 100 kcal Curd → 100 kcalTotal ≈ 300 kcal")
elif P=="M" and C==12:
	print("you can have Lunch — 200–650 kcal 2 roti → 200 kcal Dal → 200 kcal Sabzi → 100 kcal Curd → 100 kcalTotal ≈ 200 kcal")
elif P=="F" and C==12:
	print("you can have Lunch — 100–650 kcal 2 roti → 200 kcal Dal → 200 kcal Sabzi → 100 kcal Curd → 100 kcalTotal ≈ 100 kcal")
else:
	print("you cannot have lunch")






