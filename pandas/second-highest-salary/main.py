import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    employee.drop_duplicates(subset=['salary'], keep='first',inplace = True)
    try:
        salary = list(employee.sort_values(by = 'salary', ascending=False)['salary'])[1]
    except:
        salary = None
    df = pd.DataFrame({
        'SecondHighestSalary':[salary]
    })
    return df