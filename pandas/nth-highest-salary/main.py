import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    employee.drop_duplicates(subset=['salary'], keep='first',inplace = True)
    try:
        salary = list(employee.sort_values(by = 'salary', ascending=False)['salary'])[N-1]
    except:
        salary = None
    df = pd.DataFrame({
        f'getNthHighestSalary({N})':[salary]
    })
    return df