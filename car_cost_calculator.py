import requests


def calculate_loan_cost(loan_amount, interest_rate, loan_length_months, down_payment, annual_maintenance_cost, full_insurance_cost):
    monthly_interest_rate = interest_rate / 12 / 100
    print("interest_rate: {:.2f}".format(interest_rate))
    print("monthly_interest_rate: {:.2f}".format(monthly_interest_rate))
    loan_term_in_years = loan_length_months / 12
    monthly_payment = loan_amount * (monthly_interest_rate * (1 + monthly_interest_rate)
                                     ** loan_length_months) / ((1 + monthly_interest_rate)**loan_length_months - 1)

    total_loan_cost = monthly_payment * loan_length_months + down_payment
    total_maintenance_cost = annual_maintenance_cost * loan_term_in_years
    total_insurance_cost = full_insurance_cost * loan_term_in_years

    return total_loan_cost + total_maintenance_cost + total_insurance_cost


def calculate_lease_cost(lease_length, monthly_lease_payment, down_payment, annual_maintenance_cost, full_insurance_cost):
    total_lease_cost = lease_length * 12 * monthly_lease_payment + down_payment
    total_maintenance_cost = annual_maintenance_cost * lease_length
    total_insurance_cost = full_insurance_cost * lease_length

    return total_lease_cost + total_maintenance_cost + total_insurance_cost


def calculate_purchase_cost(purchase_price, annual_maintenance_cost, liability_insurance_cost, years_of_ownership):
    total_maintenance_cost = annual_maintenance_cost * years_of_ownership
    total_insurance_cost = liability_insurance_cost * years_of_ownership

    return purchase_price + total_maintenance_cost + total_insurance_cost


def get_average_interest_rate(api_key, series_id):
    url = f"https://api.stlouisfed.org/fred/series/observations?series_id={series_id}&api_key={api_key}&file_type=json&observation_start=2023-01-01"
    print(url)
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception(
            f"Error fetching interest rate data: {response.status_code}")

    data = response.json()
    observations = data["observations"]
    interest_rates = [float(obs["value"])
                      for obs in observations if obs["value"] != "."]

    return sum(interest_rates) / len(interest_rates) / 100
