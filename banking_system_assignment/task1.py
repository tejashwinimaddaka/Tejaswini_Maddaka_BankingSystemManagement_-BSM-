credit_score=float(input('Enter the credit score of a customer : '))
annual_income=float(input('Enter the annual income of the customer : '))
if credit_score>700:
    if annual_income>=50000:
        print('Eligible for a loan')
    else:
        print('Ineligible for a lone due to low annual income')
else:
    print('Ineligible for a loan')