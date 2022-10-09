import hcl2
from pathlib import Path
import os

OS_USER = os.getenv("USER")
path = Path(f"/home/{OS_USER}/terraform/").mkdir(parents=True, exist_ok=True)
print(f"Your Terraform files are stored in: '/home/{OS_USER}/terraform/'")


def main():
    with open("main.tf", "w") as file:
        main_file = hcl2.load(file)

def providers():
    with open("providers.tf", "w") as file:
        providers_file = hcl2.load(file)
        
def vars():
    with open("variables.tf", "w") as file:
        vars_file = hcl2.load(file)
