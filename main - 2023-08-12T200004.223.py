def qualify_fha_loan(credit_score, debt_to_income_ratio, employment_stability_years):
    # FHA loan requirements
    min_credit_score = 580
    max_debt_to_income_ratio = 43  # Percentage
    min_employment_stability_years = 2

    # Check credit score
    if credit_score >= min_credit_score:
        # Check debt-to-income ratio
        if debt_to_income_ratio <= max_debt_to_income_ratio:
            # Check employment stability
            if employment_stability_years >= min_employment_stability_years:
                return True  # Qualified for FHA loan
    return False  # Not qualified for FHA loan

# Input values from the couple
credit_score = int(input("Enter your credit score: "))
debt_to_income_ratio = float(input("Enter your debt-to-income ratio (%): "))
employment_stability_years = int(input("Enter years of employment stability: "))

if qualify_fha_loan(credit_score, debt_to_income_ratio, employment_stability_years):
    print("Congratulations! You qualify for an FHA loan.")
else:
    print("Sorry, you do not qualify for an FHA loan based on the provided information.")
