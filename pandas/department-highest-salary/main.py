import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(employee, department, left_on = 'departmentId', right_on = 'id')
    result_df = df.groupby('name_y').apply(lambda x:x[x['salary'] == x['salary'].max()])
    return result_df[['name_y', 'name_x','salary']].rename(columns={'name_y':'Department','name_x':'Employee','salary':'Salary'})
