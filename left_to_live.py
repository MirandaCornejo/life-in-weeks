age = input("What is your current age? ")

years=90
months=12
weeks=52
days=365

age1=int(age)

year=years-age1

day=days*year

month=year*months

week=weeks*year

age_end=print(f"You have {day} days, {week} weeks, and {month} months left.")



