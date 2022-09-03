import pymongo as pm
import pandas as pd
import certifi
import time
import selenium
from selenium import webdriver
import datetime
import regions

def get_post_info(keyword: str, start_date: str, end_date: str, pages: int) -> pd.DataFrame:
    total_header = []
    total_contents = []
    total_date = []
    driver = webdriver.Chrome("./2021-2-OSSP2-Coconut-1/Preprocessing/Crawling/Driver/chromedriver_94.exe")


    for j in range(1, pages + 1):
        # first page
        first_url = f"https://section.blog.naver.com/Search/Post.nhn?pageNo=1&rangeType=PERIOD&orderBy=sim&startDate="                     f"{start_date}&endDate={end_date}&keyword={keyword}"
        # After first page
        loop_url = f"https://section.blog.naver.com/Search/"                    f"Post.nhn?pageNo={j}&rangeType=PERIOD&orderBy=sim&startDate="                    f"{start_date}&endDate={end_date}&keyword={keyword}"
        driver.get(first_url)

        if j != 1:
            driver.get(loop_url)

        # loading...
        time.sleep(1.5)

        # crawling informations on each 7 contents
        # if any selector does not exist, that selector returns blank string
        for i in range(1, 8):
            time.sleep(1)
            try:
                head = driver.find_element_by_css_selector(
                    f"#content > section > div.area_list_search > div:nth-child({i}) > div > div.info_post > div.desc > a.desc_inner > strong > span").text
            except selenium.common.exceptions.NoSuchElementException:
                head = " "
            try:
                contents = driver.find_element_by_css_selector(
                    f"#content > section > div.area_list_search > div:nth-child({i}) > div > div.info_post > div.desc > a.text").text
            except selenium.common.exceptions.NoSuchElementException:
                contents = " "
            try:
                date = driver.find_element_by_css_selector(
                    f"#content > section > div.area_list_search > div:nth-child({i}) > div > div.info_post > div.writer_info > span.date").text
            except selenium.common.exceptions.NoSuchElementException:
                date = " "

            time.sleep(1)
            print(head)
            print(contents)
            print(date)
            total_header.append(head)
            total_contents.append(contents)
            total_date.append(date)

    return total_header, total_contents, total_date

def crawl(client):
    region_list = regions.get_regions()
    
    #지역별 업데이트
    for region in region_list:

        print(region+" 업데이트중")

        db = client["crawling_data"]
        col = db[region]
        
        s = region.split('_')
        keyword = s[0] + " " + s[1] + " " + "여행"

        #데이터중 가장 최신 데이터의 날짜에서 하루 더한값을 검색 시작일로 지정
        latest_date = col.find({},{'date':1}).sort('date',-1)[0]['date'].split('.')
        start_date = (datetime.date(int(latest_date[0]), int(latest_date[1]), int(latest_date[2]))+datetime.timedelta(days=1)).isoformat()

        #업데이트 되는 날짜를 검색 종료일로 지정
        end_date = datetime.datetime.now().strftime("%Y-%m-%d")

        #업데이트 데이터는 이전 기록과 섞이게 하기위해 1/5인 200개로 제한
        pages = 200

        #크롤링
        total_header, total_contents, total_date = get_post_info(keyword, start_date, end_date, pages)

        overlap_check={}
        
        #데이터 삽입
        for row_data in zip(total_header, total_contents, total_date):
            if row_data[0] == " ":
                break
            elif row_data[0] in overlap_check:
                continue
            else:
                overlap_check[row_data[0]] = 0
            insert_data = {'header':str(row_data[0]), "contents":str(row_data[1]), "date":str(row_data[2])}
            col.insert_one(insert_data)