def dog_to_human_years(dog_years):
    if dog_years <= 0:
        return "Please enter a valid positive number for dog years."

    if dog_years <= 2:
        human_years = 10.5 * dog_years
    else:
        human_years = 10.5 * 2 + 4 * (dog_years - 2)

    return f"{dog_years} dog years is approximately {human_years:.2f} human years."

# Example usage
dog_age = float(input("Enter dog's age in years: "))
result = dog_to_human_years(dog_age)
print(result)
