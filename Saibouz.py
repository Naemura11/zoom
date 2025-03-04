from selenium import webdriver
# from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.options import Options
import requests
import base64, json

class Saibouzmeeting_data():
    def __init__(self,saibouz_url,zoom_room_no,zoomroom,meeting_title,data_element) -> None:
        self.saibouz_url = saibouz_url
        self.zoom_room_no = zoom_room_no
        self.zoomroom = zoomroom
        self.meeting_title = meeting_title
        self.data_element = data_element

def main(URLy, rogin, Passwor):
    # draemon関数の呼び出し
    meetintg_ss:Saibouzmeeting_data
    meetintg_ss = garoonapi(URLy, rogin, Passwor)


def garoonapi(URLy,rogin,Passwor):
    message = ""
    
    
    
# 黒川君から取得したデータ   
# 会議
def get_event(day, username , password):
    URL = 'http://portal.atmj.co.jp/cgi-bin/cbgrn/grn.cgi/api/v1/schedule/events'
    autho = base64.b64encode(f'{username}:{password}'.encode()).decode()
    # ヘッダーを定義
    header = {
        'Host': 'portal.atmj.co.jp:443',
        'Content-Type': 'application/json',
        'X-Cybozu-Authorization': autho
    }
    # パラメータを定義
    params = {
        # 'target': '8673',  # 引数で指定した施設ID
        # 'targetType': 'user',  # ターゲットを施設に指定
        'orderBy': 'start desc',  # スタート時間でソート
        'rangeStart': f'{day}T00:00:00+09:00',  # 会議開始時間（範囲）
        'rangeEnd': f'{day}T23:59:59+09:00'  # 会議終了時間（範囲）
    }
    try:
        # GETリクエストを送信
        response = requests.get(URL, headers=header, params=params)
        # レスポンスのステータスコードをチェック
        if response.status_code == 200:
            # レスポンスの内容を表示
            # print(response.json().get('events', {}).get('subject', {}))
            # json_path = "C:\\Users\\777812\\Downloads\\cyb.json"
            resoponse_json = response.json()
            # with open(json_path, 'w', encoding='utf-8') as f:
            #     json.dump(resoponse_json, f, ensure_ascii=False, indent=4)
            
            events = resoponse_json.get('events', [])
            
            return events
            # for event in events:
            #     print(event.get('start', {}).get('dateTime'))
            #     print(event.get('end', {}).get('dateTime'))
            #     print(event.get('facilities')[0].get('name'))

        else:
            print(f"Error: Received response with status code {response.status_code}")
            print(response.text)
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")

# da = get_event(day="2024-11-07", username="777812", password="777812")
# # with open(file="C:\\PythonProject\\EventAlarm\\data.json", mode="w") as f:
# with open(file="C:\\PythonProject\\EventAlarm\\data.json", mode='w', encoding='utf-8') as f:
#     json.dump(da, f, ensure_ascii=False, indent=4)
