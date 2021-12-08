# DoubanMovieListSentToLetterboxd

## 说明
爬虫豆瓣标记“看过”的影视条目信息，包括标题、IMDb ID、打分、标记时间、标签、短评，并制成CSV，可上传至Letterboxd进行同步。

## 使用方法
### 方法一
- 直接使用打包好的main.exe文件
### 方法二
- 安装python3环境
- pip安装requests、beautifulsoup4和lxml这三个第三方库
- 运行main.py

## 流程
图文并茂流程：https://www.douban.com/note/821101672/
1. 填写豆瓣用户id
2. 填写豆瓣用户cookies
3. 选择对第几页到第几页进行备份
4. 输入文件名创建csv文件
5. 等待抓取结束
6. 打开csv文件，可使用excel打开，将标记时间那一列的单元格格式改为“yyyy-mm-dd”
7. 在Letterboxd的“Settings”选项中，找到“IMPORT & EXPORT”一栏，选择“IMPORT YOUR DATA”，选择csv文件进行上传
8. 根据Letterboxd给出的信息进行细微调整，查缺补漏同步的条目，确认无误后选择“IMPORT FILMS”即可

## 注意事项
1. 爬虫速度设置得很慢，建议多次少页。
2. Letterboxd上传数据一次最多不超过1900条，豆瓣每页有15个条目，所以最好一次性不要备份超过126页。
3. 两种情况将导致缺少IMDb ID，一是条目本身无IMDb编号，二是条目已被404。建议CSV保存完毕后自行进行检查和补上。
4. 如果填写的csv文件名在同目录下存在同名文件，将会对同名文件进行覆盖。
5. Letterboxd对剧集支持度不够，即使有IMDb ID也容易出现无条目的情况。
6. 俺是个初学者，哪里做得不好还请多多见谅和多多指正。
