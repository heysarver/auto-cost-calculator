# main.py
import argparse
import os
from car_cost_calculator import calculate_loan_cost, calculate_lease_cost, calculate_purchase_cost, get_average_interest_rate

def get_argument_or_env(var_name, default_value):
    return os.environ.get(var_name, default_value)

def main():
    parser = argparse.ArgumentParser(description="Compare the total costs of leasing, getting a loan, and purchasing a car outright.")
    
    parser.add_argument("--loan_amount", type=float, default=get_argument_or_env("LOAN_AMOUNT", 25000), help="Loan amount in USD")
    parser.add_argument("--interest_rate", type=float, default=get_argument_or_env("INTEREST_RATE", 3.5), help="Annual interest rate for the loan as a percentage")
    parser.add_argument("--loan_length_months", type=int, default=get_argument_or_env("LOAN_LENGTH_MONTHS", 60), help="Loan length in months")
    parser.add_argument("--down_payment", type=float, default=get_argument_or_env("DOWN_PAYMENT", 5000), help="Down payment in USD")
    parser.add_argument("--lease_length_months", type=int, default=get_argument_or_env("LEASE_LENGTH_MONTHS", 36), help="Lease length in months")
    parser.add_argument("--monthly_lease_payment", type=float, default=get_argument_or_env("MONTHLY_LEASE_PAYMENT", 300), help="Monthly lease payment in USD")
    parser.add_argument("--purchase_price", type=float, default=get_argument_or_env("PURCHASE_PRICE", 30000), help="Car purchase price in USD")
    parser.add_argument("--annual_maintenance_cost", type=float, default=get_argument_or_env("ANNUAL_MAINTENANCE_COST", 1000), help="Annual maintenance cost in USD")
    parser.add_argument("--full_insurance_cost", type=float, default=get_argument_or_env("FULL_INSURANCE_COST", 1500), help="Annual full insurance cost in USD")
    parser.add_argument("--liability_insurance_cost", type=float, default=get_argument_or_env("LIABILITY_INSURANCE_COST", 800), help="Annual liability insurance cost in USD")
    parser.add_argument("--years_of_ownership", type=int, default=get_argument_or_env("YEARS_OF_OWNERSHIP", 5), help="Number of years of ownership for the outright purchase scenario")
    parser.add_argument("--interest_rate_series", type=str, default=get_argument_or_env("INTEREST_RATE_SERIES", "CARACBW027SBOG"), help="Interest rate series identifier")
    parser.add_argument("--fred_api_key", type=str, default=get_argument_or_env("FRED_API_KEY", None), help="FRED API key to fetch the average interest rate")

    args = parser.parse_args()

    if args.fred_api_key:
        series_id = args.interest_rate_series
        args.interest_rate = get_average_interest_rate(args.fred_api_key, series_id)

    loan_cost = calculate_loan_cost(args.loan_amount, args.interest_rate, args.loan_length_months, args.down_payment, args.annual_maintenance_cost, args.full_insurance_cost)
    lease_cost = calculate_lease_cost(args.lease_length_months, args.monthly_lease_payment, args.down_payment, args.annual_maintenance_cost, args.full_insurance_cost)
    purchase_cost = calculate_purchase_cost(args.purchase_price, args.annual_maintenance_cost, args.liability_insurance_cost, args.years_of_ownership)

    print("Total cost of getting a loan: ${:.2f}".format(loan_cost))
    print("Total cost of leasing a car: ${:.2f}".format(lease_cost))
    print("Total cost of purchasing a car outright: ${:.2f}".format(purchase_cost))

if __name__ == "__main__":
    main()
