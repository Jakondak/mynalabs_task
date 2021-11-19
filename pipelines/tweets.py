import os
import pandas as pd
import re

def remove_emojis(data):
    emoj = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U00002500-\U00002BEF"  # chinese char
        u"\U00002702-\U000027B0"
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        u"\U0001f926-\U0001f937"
        u"\U00010000-\U0010ffff"
        u"\u2640-\u2642" 
        u"\u2600-\u2B55"
        u"\u200d"
        u"\u23cf"
        u"\u23e9"
        u"\u231a"
        u"\ufe0f"  # dingbats
        u"\u3030"
                      "]+", re.UNICODE)
    return re.sub(emoj, '', data)


def tweets_wo_url(user_name, from_date, end_date, max_results):
    # Создаю и запускаю скрапер твитов
    user_tweets = "snscrape --format '{content!r}'" + \
                  f" --max-results {max_results} --since {from_date}" \
                  f" twitter-user '{user_name} until:{end_date}'" \
                  f" > user-tweets.txt"
    os.system(user_tweets)
    df = pd.read_csv("user-tweets.txt", names=["content"])
    final_list = []
    for row_number in range(df.shape[0]):
        row = df.iloc[row_number]["content"]
        row_wo_url = re.sub(r"http\S+", "", row[1:-1].strip())
        row_wo_emojii = remove_emojis(row_wo_url)

        if len(row_wo_emojii) > 3:
            final_list.append(row_wo_emojii)

    return final_list
