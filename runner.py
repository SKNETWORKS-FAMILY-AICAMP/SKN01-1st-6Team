from helpers.ui import Ui
#from streamlit.web.cli import main

# from helpers.carcrawling import 수집
# from helpers.db import MySQLDatabase
# from helpers.db import *



if __name__ == "__main__":
    #01 스트림릿 클래스
    # 전국 자동차 등록 현황 및 기업 FAQ 조회 시스템
    ui = Ui("Crawling Project (SKN01-1st-6Team)")

    #02
    # 수집()

    #03 디비에저장
    # try:
    #     user = "root"
    #     password = ""
    #     host = "localhost"
    #     port = 3306
    #     db = "test"

    #     db_url = f"mysql+pymysql://{user}:{password}@{host}:{port}/{db}"
    #     db = MySQLDatabase(db_url)

    #     print(db.__repr__)
    #     import sys
    #     sys.exit()        

    #     db.to_sql()

    #     # db.add_user("john_doe", "john@example.com")
    #     # user =  db.get_user_by_username("john_doe")
    #     # print(user.username, user.email)
    #     # db.update_user_email("john_doe", "new_email@example.com")
    #     # user =  db.get_user_by_username("john_doe")
    #     # print(user.username, user.email)

    #     # db.delete_user("john_doe")

    # except Exception as e:
    #     print("DB부분처리안됨")    
    #     print("e")
    
    #04 디비2로 저장
    #테이블에레코드인서트할때()


   
