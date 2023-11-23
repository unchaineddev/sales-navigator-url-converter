# Extracts links from csv file 

import pandas as pd 

def links():
    df = pd.read_csv('lsn-links/links.csv')
    profiles = df['PROFILE_VISITE']
    print(profiles)
    return profiles

