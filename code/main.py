from DoubanMovieListCrawler import *
import csv


def main():
    user_id = input("----------------------------------------------------\n"
                    "请输入豆瓣用户id：")

    start_page_number = int(input("----------------------------------------------------\n"
                                  "请输入从第几页开始备份（输入数字即可）："))
    start_number = (start_page_number - 1) * 15
    end_page_number = int(input("----------------------------------------------------\n"
                                "请输入备份到第几页（输入数字即可）："))
    end_number = (end_page_number - 1) * 15

    file_name = input("----------------------------------------------------\n"
                      "请创建CSV的文件名(无需添加.csv后缀)：")
    f = open(f"{file_name}.csv", "w", newline="", encoding="utf_8_sig")
    csv_write = csv.writer(f)
    csv_head = ["Title", "imdbID", "Rating", "WatchedDate", "Tags", "Review"]
    csv_write.writerow(csv_head)
    f.flush()

    while start_number <= end_number:
        watched_to_notion = DoubanCrawler(start_number=start_number)
        watched_url = f"https://movie.douban.com/people/{user_id}/collect?start={start_number}&sort=time&rating=all&filter=all&mode=grid"
        watched_to_notion.req(url=watched_url, file_name=file_name)
        start_number += 15

    f.close()
    input("按Enter回车键退出")
    exit()


def add_cookies():
    cookies_str = input('----------------------------------------------------\n'
                        '请输入你的豆瓣cookies:')
    if cookies_str[0:3] == "ll=":
        cookies_dict = {}
        cookies_list = cookies_str.split('; ')
        for i in cookies_list:
            name, value = i.split('=', 1)
            cookies_dict[f'{name}'] = value
        return cookies_dict
    else:
        print("你输入的豆瓣cookies可能有误，请再重新试试吧！")
        add_cookies()


if __name__ == "__main__":
    main()