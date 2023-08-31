import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    df = scores.drop(columns=['id']).sort_values(by = 'score',ascending=False)
    unique_score_values = df['score'].unique()
    map_df = pd.DataFrame({
    'score_value':unique_score_values
    })
    df['rank'] = df['score'].map( lambda x : map_df[map_df['score_value'] == x].index[0] +1 )
    return df
