
from prettytable import PrettyTable
    
x = PrettyTable()

x.field_names = ["Domain", "Left Days", "Signer", "Health"]

x.add_row(["Tvsmotor.com", 129, "Golbal Sign", "A"])


print(x)