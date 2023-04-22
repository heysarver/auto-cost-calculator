# auto-cost-calculator
A tool that compares the costs of buying vs. leasing vs. car loans.

## Arguments

| CLI Parameter                | Environment Variable   | Default Value |
|------------------------------|------------------------|---------------|
| `--loan_amount`              | `LOAN_AMOUNT`          | 25000         |
| `--interest_rate`            | `INTEREST_RATE`        | *Fetched from API* |
| `--loan_length_months`       | `LOAN_LENGTH_MONTHS`   | 60            |
| `--down_payment`             | `DOWN_PAYMENT`         | 5000          |
| `--lease_length_months`      | `LEASE_LENGTH_MONTHS`  | 36            |
| `--monthly_lease_payment`    | `MONTHLY_LEASE_PAYMENT`| 300           |
| `--purchase_price`           | `PURCHASE_PRICE`       | 30000         |
| `--annual_maintenance_cost`  | `ANNUAL_MAINTENANCE_COST` | 1000       |
| `--full_insurance_cost`      | `FULL_INSURANCE_COST`  | 1500          |
| `--liability_insurance_cost` | `LIABILITY_INSURANCE_COST` | 800       |
| `--years_of_ownership`       | `YEARS_OF_OWNERSHIP`   | 5             |
| `--fred_api_key`             | `FRED_API_KEY`         | *Required*    |
| `--interest_rate_series`     | `INTEREST_RATE_SERIES` | CARACBW027SBOG |

## Interest Rate Series Mapping

You can search for more series identifiers on the FRED website: https://fred.stlouisfed.org/

Please note that the availability and update frequency of these series identifiers may vary.
