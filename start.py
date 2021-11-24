from datetime import date
from pipelines.tweets import tweets_wo_url
from pipelines.lyrics import lyrics_sentence
import pandas as pd


def start():
    # Запускаю парсер твитеров
    END_DATE = date.today()
    FROM_DATE = "2017-01-01"
    MAX_RESULTS = 10
    USER_NAME = "nickiminaj"
    tweets_list = tweets_wo_url(USER_NAME, FROM_DATE, END_DATE, MAX_RESULTS)

    # Запускаю парсер песен
    LINK = "https://www.azlyrics.com/n/nickiminaj.html"
    TIME_SLEEP = 5
    lyrics_list = lyrics_sentence(LINK, TIME_SLEEP)

    # Сохраняю финальный датасет
    data_for_df = tweets_list + lyrics_list
    df = pd.DataFrame(data_for_df, columns=['Text'])
    df = df.drop_duplicates()
    df.to_csv('df.csv')


if __name__ == "__main__":
    start()
