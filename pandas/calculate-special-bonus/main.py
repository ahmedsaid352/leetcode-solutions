import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = employees[(employees['employee_id']%2 != 0) & (employees['name'].str.startswith('M') == False)][['salary']]
    employees.fillna(0, inplace=True)
    employees.bonus = employees.bonus.astype(int)
    return employees[['employee_id','bonus']].sort_values(by = 'employee_id')