import pandas as pd
from tweets_to_topic_network.topic import Topic_modeler
import sys

file_tweets = '/Users/alessiogandelli/data/cop_merged/cop_merged_original.pkl'

#file_tweets = sys.argv[1]

print(file_tweets)

df = pd.read_pickle(file_tweets)

# df = df[df['referenced_type'].isna()]

folder_path = file_tweets.split('/')[:-1]
folder_path = '/'.join(folder_path)
print(folder_path)

def lang_distribution():

    s = df['lang'].value_counts()#.head(20)

    s = s / s.sum()

    #merge all together the languages that are not in the top 10
    n = 8
    top = s[:n]

    # Get the sum of the rest of the entries
    others = pd.Series([s[n:].sum()], index=['others'])

    # Create a new series with the first 9 entries and the sum of the others
    s_new = pd.concat([top, others])

    # Convert the series to a DataFrame and transpose it
    df_lang = s_new.to_frame().T

    # Create a horizontal stacked bar plot
    ax = df_lang.plot.bar(stacked=True, legend=False)

    #change size 
    fig = ax.get_figure()
    fig.set_size_inches(3, 12)

    for rect in ax.patches:
        h = rect.get_height()
        if h > 0.02:  # Only add labels when the segment is large enough
            x = rect.get_x()
            y = rect.get_y()
            ax.text(x+0.1, y+h-0.01, f'{h:.1%}', va='center')

    # Add the legend
    ax.legend(title='Language', bbox_to_anchor=(1, 1), loc='upper left')

    return df_lang


lang_distribution()


