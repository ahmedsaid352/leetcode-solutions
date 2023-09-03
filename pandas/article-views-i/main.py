import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    ids = views[views['author_id'] ==views['viewer_id'] ]['viewer_id']
    df = pd.DataFrame({
        'id':ids
    })
    return df.sort_values(by = 'id').drop_duplicates()