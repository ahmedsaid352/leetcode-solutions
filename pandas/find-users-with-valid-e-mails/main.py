import pandas as pd
import re

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    valid = users[users['mail'].str.contains(r'^[a-zA-Z][a-zA-Z0-9_.\-]*@leetcode\.com',regex = True)]
    return valid