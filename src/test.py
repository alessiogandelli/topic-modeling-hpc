import pandas as pd
from tweets_to_topic_network.topic import Topic_modeler



file_tweets = '/Users/alessiogandelli/data/cop23/cache/data/tweets_cop23.pkl'      

df = pd.read_pickle(file_tweets)

df = df[df['referenced_type'].isna()]

tm = Topic_modeler(df, name = 'cop23', embedder_name='all-MiniLM-L6-v2', path_cache = '/Users/alessiogandelli/data/cop23/cache')


print('done')