name_and_score = {"Derek": 7, "Xavier": 80, "Bob": 612, "Chantanelle": 9}

sorted_names = sorted(name_and_score.keys())

for name in sorted_names:
    print(f"{name} = {name_and_score[name]}")

if