#%%
import pandas as pd
from tweets_to_topic_network.topic import Topic_modeler
import sys
import os

file_tweets = sys.argv[1] 

df = pd.read_pickle(file_tweets)

df = df[df['referenced_type'].isna()]

#get folder path
folder_path = file_tweets.split('/')[:-1]
folder_path = file_tweets.split('/')[:-1]
folder_path = '/'.join(folder_path)
path_cache = os.path.join(folder_path, 'cache')

print(path_cache)

# %%

tm = Topic_modeler(df, name = 'cop_merged', embedder_name='all-MiniLM-L6-v2', path_cache = path_cache)
df_labeled = tm.get_topics()

# %%
tm = Topic_modeler(df, name = 'cop_merged', embedder_name='paraphrase-MiniLM-L3-v2', path_cache = path_cache)
df_labeled = tm.get_topics()

# %%

# tm = Topic_modeler(df, name = 'cop_merged', embedder_name='text-embedding-3-small', path_cache = path_cache)
# df_labeled = tm.get_topics()


# %%
# tm.docs is a list of strings get the lenght of each 

len_docs = [len(doc) for doc in tm.docs]
# %%


# %%
