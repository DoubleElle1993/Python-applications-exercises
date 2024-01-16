import numpy as np
import pandas as pd
import time

df = pd.DataFrame(np.random.randint(0, 30, size=(5000, 4)), columns=('a','b','c','d'))

def loop(df):
    """
    Create new column to find the ratio between column D and C loops
    """
    start = time.time()
    for idx, row in df.iterrows():
        df.at[idx, 'ratio'] = 100 * (row['d'] / row['c'])

    end = time.time()
    print(end - start)



def vectorization(df):
    """
    Create new column to find the ratio between column D and C using vectorization
    """

    start = time.time()

    df['ratio'] = 100 * (df['d'] / df['c'])

    end = time.time()
    print(end - start)