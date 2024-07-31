import requests
import time
from prettytable import PrettyTable

subdomains = ["sub1.awesomeweb:8080", "sub2.awesomeweb:8080", "sub3.awesomeweb:8080"]

def check_subdomains():
    table = PrettyTable()
    table.field_names = ["Subdomain", "Status"]
    for subdomain in subdomains:
        try:
            response = requests.get(f"http://{subdomain}")
            status = "Up" if response.status_code == 200 else "Down"
        except requests.ConnectionError:
            status = "Down"
        except Exception as e:
            status = f"Error: {e}"
        table.add_row([subdomain, status])
    print(table)

if __name__ == "__main__":
    while True:
        check_subdomains()
        time.sleep(60)
