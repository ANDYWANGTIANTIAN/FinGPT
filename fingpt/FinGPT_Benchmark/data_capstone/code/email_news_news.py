import pandas as pd
import re
df=pd.read_csv('Email.CSV')
df.rename(columns={'ÕýÎÄ':'content'},inplace=True)
df=df[['content']]


def remove_link(text):
    return re.sub(r'<.*?>', '', text)

df['content'] = df['content'].apply(remove_link)
print(df['content'].head())
df = df.dropna(subset=['content'])
df.to_csv('email_clean.csv')



