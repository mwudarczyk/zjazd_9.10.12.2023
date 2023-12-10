import biblioteki as pd

df = pd.read_csv('weight-height.csv')
print(df.head(15))
print(df.Gender.value_counts())
df.Height += 2.54
df.Weight /= 2.2
print(df)

print(df.describe().T.to_string())
df = pd.get_dummies(df)
print(df)
df['new'] = df.Weight - 100
del (df['Gender_Male'])
print(df)
df.rename(columns= {'Gender_Female': 'Gender'}, inplace=True)
print(df)