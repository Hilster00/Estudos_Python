df = pd.DataFrame({'Idade': [25, 30, 35, 40], 'Altura': [1.80, 1.70, 1.75, 1.78]})

# Formato 'records'
dict_records = df.loc[:, ['Idade', 'Altura']].to_dict(orient='records')
print(dict_records)

# Formato 'dict'
dict_dict = df.loc[:, ['Idade', 'Altura']].to_dict(orient='dict')
print(dict_dict)

# Formato 'list'
dict_list = df.loc[:, ['Idade', 'Altura']].to_dict(orient='list')
print(dict_list)

