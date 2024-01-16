#Imagine we want to create a new column ‘e’ based on some conditions on the exiting column ‘a’.

import pandas as pd
import numpy as np
import time

df = pd.DataFrame(np.random.randint(1, 10, size=(100, 4)), columns=['AA', 'BB', 'CC', 'DD'])

def loop():
    """
    Create new column based on a logical condition using loop
    """


    start = time.time()
    for idx, row in df.iterrows():
        if row['AA'] == 4:
            df.at[idx, 'EE'] = row['BB']
        elif row['CC'] == 7:
            df.at[idx, 'EE'] = row['AA']
        else:
            df.at[idx, 'EE'] = 'AAA'

    end = time.time()

    print(end-start)


def vectorization():
    """
    Create new column based on a logical condition using vectorization
    """


    start = time.time()

    df.loc[df['AA'] == 9, 'EE'] = df['BB']
    df.loc[df['CC'] == 7, 'EE'] = df['AA']
    df.loc['EE'] = 'AAA'

    end = time.time()
    print(end - start)

