company_users = {}
command = input()
while command != "End":
    company_names, employees_id = command.split(" -> ")
    if company_names not in company_users:
        company_users[company_names] = []
    if employees_id not in company_users[company_names]:
        company_users[company_names].append(employees_id)
    command = input()
for company_name, employee_id in company_users.items():
    print(company_name)
    for employee in employee_id:
        print(f"-- {employee}")

