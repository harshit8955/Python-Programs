import pandas as pd

data = pd.read_csv("emails.csv") 
#it require a csv file to send eamils.

for email in data["email"]:
    print(email)