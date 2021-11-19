import requests
from bs4 import BeautifulSoup
import time


def lyrics_sentence(link, time_sleep):
    r = requests.get(link)
    page = BeautifulSoup(r.text, "html.parser")
    final_list = []
    for link in page("a"):
        try:
            if "lyrics/nickiminaj/" in link["href"]:
                link = 'https://www.azlyrics.com' + link["href"][2:]
                time.sleep(time_sleep)
                link_r = requests.get(link)
                link_page = BeautifulSoup(link_r.text, "html.parser")

                # Мне нужны таки песни, где поет только Ники, чтобы не было чужих слов. Т.е. нужно убрать фиты (feat)
                if len(link_page.findAll("span", class_="feat")) == 0:
                    # Сразу достаю текст песни
                    text = link_page.findAll("div", class_=None)[1].text.split('\n')
                    text_wo_spaces = [line for line in text if len(line) > 3]
                    final_list.extend(text_wo_spaces)
        except KeyError:
            pass

    return final_list
