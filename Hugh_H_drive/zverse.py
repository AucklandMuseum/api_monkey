import ast
import json
import pandas as pd
from flatten_json import flatten

df = pd.read_csv("data/z20.csv", sep = ",")
print (df.head(2))
print (f"Existing columns:")
for col in df.columns: 
    print(col)
print ('\n')


(pd.json_normalize(pd.json_normalize(pd.json_normalize(kit)
                   .explode("flows")
                   .to_dict(orient="records"))
 .explode("flows.kit.products")
 .to_dict(orient="records"))
)


# multi = []; inner = {}

# def recursive_extract(i):
#     global multi, inner

#     if type(i) is list:
#         if len(i) == 1:
#             for k,v in i[0].items():
#                 if type(v) in [list, dict]:
#                     recursive_extract(v)
#                 else:                
#                     inner[k] = v
#         else:
#             multi = i

#     if type(i) is dict:
#         for k,v in i.items():
#             if type(v) in [list, dict]:
#                 recursive_extract(v)
#             else:                
#                 inner[k] = v

# print (type(df['metadata']))
# recursive_extract(df['metadata'])
# # recursive_extract(df(['metadata'],['annotations'])

# data_dict = []
# for i in multi:    
#     tmp = inner.copy()
#     tmp.update(i)
#     data_dict.append(tmp)

# print (data_dict)
# md_df = pd.DataFrame(data_dict)
# print (md_df.head())
# df.to_csv('Output.csv')

# md_dict = dict(zip(df['metadata']))
# dic_flattened = [flatten(d) for d in df]
# df = pd.DataFrame(dic_flattened)
# print (df.head())


# md_df = pd.json_normalize(df['metadata'])
# print (f"New columns: ")
# for col in md_df.columns: 
#     print(col)
# print ('\n')


# with open("data/z20.json", 'w') as f:
#     f.write(csv_frame.to_json(orient='records', lines=True))

# df = pd.read_json("z20.json")
# print ("Summary:",'\n',df.head(),'\n')

# df = pd.io.json.json_normalize(data)

# md_df = pd.json_normalize(df['metadata'].apply(json.loads).tolist())
# print (md_df.head(2))

# anno_df = pd.Series.to_frame(df['annotations'])
# print (anno_df.head(2))

# print (anno_df.info())


# def only_dict(d):
#     '''
#     Convert json string representation of dictionary to a python dict
#     '''
#     return json.loads(d)

# def list_of_dicts(ld):
#     '''
#     Create a mapping of the tuples formed after 
#     converting json strings of list to a python list   
#     '''
#     return dict([(list(d.values())[1], list(d.values())[0]) for d in json.loads(ld)])

# A = pd.json_normalize(df['metadata'].apply(only_dict).tolist()).add_prefix('md.')
# B = pd.json_normalize(df['annotations'].apply(list_of_dicts).tolist()).add_prefix('anno.')

# print (A.head(2))
# print (B.head(2))

# df = df[['classification_id']].join([A, B])

# print (df.head())

# df.to_csv('data/final.csv') 

# print ("Columns:")
# for col in dframe.columns: 
#     print(col)
# print ('\n')

# # print ("'Workflow name' column:")
# # print (dframe['workflow_name'].describe(),'\n')

# # print ("Summary:")
# # print (dframe.groupby('workflow_name')['classification_id'].nunique(),'\n')

# print ("Top 10 users:")
# n = 10
# print (dframe['user_name'].value_counts()[:n])

# fields = ["user_name","metadata.viewport","subject_ids"]
# md = pd.json_normalize(dframe[fields])
# md = pd.json_normalize(dframe)
# md = pd.concat([pd.DataFrame(pd.json_normalize(x)) for x in dframe['metadata']],ignore_index=True)
# print (md.head())

# df_anno = pd.concat([pd.DataFrame(pd.json_normalize(x)) for x in dframe['annotations']],ignore_index=True)
# print (df_anno.head())

# print ("\nAnnotations columns:")
# for col in df_anno.columns: 
#     print(col)

# if df_anno['task']== "T2":
#     print ('\n',"Table:",df_anno['value'])
# df_vals = pd.concat([pd.DataFrame(pd.json_normalize(x)) for x in df_anno['value']],ignore_index=True)

# print ("\nValue columns:")
# for col in df_vals: 
#     print(col)