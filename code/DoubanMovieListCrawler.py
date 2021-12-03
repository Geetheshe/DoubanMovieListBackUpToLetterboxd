import requests
import re
import time
import random
import csv
from bs4 import BeautifulSoup


class DoubanCrawler:
    def __init__(self, start_number):
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"}
        self.page_number = start_number / 15 + 1

    def req(self, url, file_name):
        r1 = requests.request("GET", url=url, headers=self.headers)
        print(f'看过的第{int(self.page_number)}页响应状态码：{r1.status_code}')
        list_soup = BeautifulSoup(r1.text, 'lxml')
        movies_list = list_soup.find_all("div", class_="item")
        for movie in movies_list:
            # 条目名称
            movie_title = movie.find("em").get_text()

            # 条目评分
            try:
                rating = movie.find("span", class_=re.compile("rating"))["class"]
                if rating == ['rating1-t']:
                    movie_rate = "1"
                elif rating == ['rating2-t']:
                    movie_rate = "2"
                elif rating == ['rating3-t']:
                    movie_rate = "3"
                elif rating == ['rating4-t']:
                    movie_rate = "4"
                elif rating == ['rating5-t']:
                    movie_rate = "5"
                else:
                    movie_rate = ""
            except TypeError:
                movie_rate = ""

            # 条目短评
            try:
                movie_comment = movie.find("span", class_="comment").get_text()
            except AttributeError:
                movie_comment = ""

            # 条目标签
            try:
                movie_tag = movie.find("span", class_="tags").get_text().replace("标签: ", "").replace(" ", ",")
            except AttributeError:
                movie_tag = ""

            # 条目标记时间
            movie_date = movie.find("span", class_="date").get_text()

            # 条目豆瓣链接
            movie_link = movie.find("a", href=True)["href"]

            # 获取条目详情中的IMDB链接、标签
            r2 = requests.request("GET", url=movie_link, headers=self.headers)
            print(f'《{movie_title}》的详情页访问状态为{r2.status_code}。')
            detail_soup = BeautifulSoup(r2.text, 'lxml')

            # 条目imdb id
            try:
                imdb_id = detail_soup.find("span", class_="pl", text=re.compile("IMDb")).next_sibling.lstrip()
            except AttributeError:
                imdb_id = ""

            data = open(f"{file_name}.csv", "a", newline="", encoding="utf_8_sig")
            csv_write = csv.writer(data)
            csv_head = [movie_title, imdb_id, movie_rate, movie_date, movie_tag, movie_comment]
            csv_write.writerow(csv_head)

            # 反爬休息
            time.sleep(random.randint(5, 10))