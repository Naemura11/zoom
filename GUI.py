import flet as ft
import json
import os
from pathlib import Path
# import AotomaticZoomReservation
# import Saibouzu_test


setting_front:bool = True

def main(page: ft.Page):
    # ツールスタートボタンの処理
    def handle_button_click(e):
        # 複数のボタンの機能を一つの関数で処理
        # Zoomの設定とサイボウズのログイン情報をJsonファイルに送る
        zoomsetting_json(e)
        save_to_json(e)  # JSONへ保存
        page.window_close()
        # サイボウズログインを行う関数を呼び出す
        # AotomaticZoomReservation.main(URLy.value, Login_name.value, Password.value)

    # 「設定画面の最前列表示」のボタン押下の処理
    def button_clicked(e):
        global setting_front
        if e.control == b1:
            e.page.window_always_on_top = True  # 常に最前列で表示
            setting_front = True
        elif e.control == b2:
            e.page.window_always_on_top = False  # 最前列ではない
            setting_front = False
        page.update()
    
    # Zoom会議室のオプション設定「ミーティングを自動的に記録」のチェックボタン押下の否かでラジオボタン出現判断
    def checkbox_changed(e):
        if c5.value:
            # ラジオボタンを表示
            radio_group.visible = True
        else:
            # ラジオボタンを非表示
            radio_group.visible = False
        page.update()
    
    # 設定画面の「この設定を記憶する」の内容の条件分岐・Jsonファイルに書き込み
    def zoomsetting_json(e):
        # 記憶する場合
        if cg.value == '記憶する':
            setting_waiting = c1.value
            setting_authentic = c2.value
            setting_anytime = c3.value
            setting_mute = c4.value
            setting_record = c5.value
            setting_localorcloud = radio_group.value   
            global setting_front

            # 新しいデータを辞書に保存
            setting_zoom = {
                'Zoom_Waiting_Room_Check':setting_waiting,
                'Zoom_Require_Authenti_Check': setting_authentic, 
                'Approval_Anytime_Join_Check': setting_anytime,
                'Zoom_Mute': setting_mute,
                'Zoom_Record':setting_record,
                'Zoom_Record_detail':setting_localorcloud,
                'Tool_Front':setting_front
            }
            # # JSONファイル名
        else:  
            # 記憶しない選択の場合
            # デフォルト設定に戻す
            setting_waiting = False
            setting_authentic = False
            setting_anytime = True
            setting_mute = False
            setting_record = False
            setting_localorcloud = "local"   
            setting_front=True

            # 新しいデータを辞書に保存
            setting_zoom = {
                'Zoom_Waiting_Room_Check':setting_waiting,
                'Zoom_Require_Authenti_Check': setting_authentic, 
                'Approval_Anytime_Join_Check': setting_anytime,
                'Zoom_Mute': setting_mute,
                'Zoom_Record':setting_record,
                'Zoom_Record_detail':setting_localorcloud,
                'Tool_Front':setting_front
            }
        # JSONファイル名
        json_file_name = Path("ZoomSetting.json")

        # JSON形式でファイルに保存
        with open(json_file_name, 'w', encoding='utf-8') as json_file:
            json.dump(setting_zoom, json_file, ensure_ascii=False, indent=4)  # 日本語を含む場合はensure_ascii=False
        page.update()  # 表示を更新

    # Jsonファイルに保存されたZoom会議室の設定情報の読み込み、返り値として渡す処理
    def get_setting_zoom() -> dict:
        # JSONファイル名
        json_file_name = "ZoomSetting.json"
        # ファイルパスの指定
        os.getcwd()
        # print(os.getcwd())
        json_file_path = os.path.abspath(json_file_name)

        if os.path.exists(json_file_path):
            # 既存のデータを読み込む
            with open(json_file_name, 'r', encoding='utf-8') as json_file:
                zoomdata = json.load(json_file)

                zoomwait = zoomdata['Zoom_Waiting_Room_Check']
                zoomrequire = zoomdata['Zoom_Require_Authenti_Check']
                zoomanytime = zoomdata['Approval_Anytime_Join_Check']
                zoommute = zoomdata['Zoom_Mute']
                zoomrecord = zoomdata['Zoom_Record']
                zoomdetail = zoomdata['Zoom_Record_detail']
                toolfront = zoomdata['Tool_Front']
            return zoomwait, zoomrequire, zoomanytime,zoommute,zoomrecord,zoomdetail,toolfront
        
    # サイボウズログイン情報をjsonファイルに書き込む関数
    def save_to_json(e):
        # ユーザーが入力した情報を取得
        setting_login_name = Login_name.value
        setting_password = Password.value
        
        # 新しいデータを辞書に保存
        new_data = {
            'Login_name': setting_login_name,
            'Password': setting_password
        }

        # JSONファイル名
        json_file_name = "Saibouz_login.json"
        # JSON形式でファイルに保存
        os.getcwd()
        json_file_path = os.path.abspath(json_file_name)

        with open(json_file_path, 'w', encoding='utf-8') as json_file:
            json.dump(new_data, json_file, ensure_ascii=False, indent=4)  # 日本語を含む場合はensure_ascii=False

    # Jsonファイルに記載されているログイン名とパスワードを取得する 
    def get_login_data():
        # JSONファイル名
        json_file_name = Path("Saibouz_login.json")
        # Jsonファイルからログインとパスワードの取得
        if os.path.exists(json_file_name):
            # 既存のデータを読み込む
            with open(json_file_name, 'r', encoding='utf-8') as json_file:
                data = json.load(json_file)
                login_id = data['Login_name']
                login_password = data['Password']
            return login_id, login_password

    
    # ページ設定(初期値)===============================
    page.title = "AZR(アズール)"
    page.bgcolor = ft.colors.BLUE_100
    page.window.width = 400  # 幅 500
    page.window.height = 300  # 高さ 400にする
    page.window.resizable = True  # ウィンドウサイズ変更可否
    # 最初の表示位置
    page.window_top = 90

    # 余白
    page.padding = 10
    # ページの最小値
    page.window.min_width = 400
    page.window.min_height = 300

    # 設定画面とツールスタートボタン処理==============
    # 設定画面の文字のテキスト処理
    t1 = ft.Text(
        "設定画面",
        size=16,  # サイズ
        weight=ft.FontWeight.BOLD,
        color=ft.colors.BLACK87,  # 太さ
        selectable=True  # 選択可否(default:False)   
    )
    # t1をContainerでラップし、枠線を追加
    t1_container = ft.Container(
        content=t1,
        padding=16,
        bgcolor=ft.colors.WHITE,  # 内側の余白
        border=ft.border.all(2, ft.colors.BLACK)               
    )
    # ツールスタートボタンの処理
    b5 = ft.ElevatedButton(
        content=ft.Text(
            "ツールスタート",
            size=24
        ), 
        on_click=handle_button_click, 
        style=ft.ButtonStyle(
            color=ft.colors.BLACK,  # 文字色
            bgcolor=ft.colors.BLUE_400,  # 背景色
            padding=16,  # ボタン内部の余白を増やす
            shape=ft.RoundedRectangleBorder(radius=0)
        )
    )

    # 設定画面とツールスタートボタンのレイアウト
    setting_container = ft.Row(
        controls=[t1_container, b5],
        # 設定画面のテキストとボタンの間のスペース
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    )

    # サイボウズURL貼り付け欄の処理===================
    # テキスト
    saibouzu_text = ft.Text(
        "サイボウズのURLの貼り付け:",
        size=15,
        weight=ft.FontWeight.W_400
    )
    # URL貼り付け欄
    URLy = ft.TextField(expand=True)
    url_container = ft.Row(
        controls=[saibouzu_text,URLy],
        spacing=15  
    )
    # テキストとURL貼り付け欄のコンテナ
    container = ft.Container(
        content=url_container,  # RowをContainerのコンテンツとして指定
        padding=10,       # 内側の余白
        bgcolor=ft.colors.WHITE,  # Containerの背景色を白に設定
        border=ft.border.all(2, ft.colors.BLACK)  # 黒の枠線
    )
    # 「Zoom会議室の設定」のテキスト==============
    zoom_text = ft.Text(
        "Zoom会議室の設定",
        size=15,
        weight=ft.FontWeight.W_400
    )
    # 「Zoom会議室の設定」のテキストの外側の枠線
    zoom_text_container = ft.Container(
        content=zoom_text,
        padding=10,
        bgcolor=ft.colors.WHITE,  # 内側の余白
        border=ft.border.all(2, ft.colors.BLACK) # 黒の枠線
    )
    # 次回以降もこの設定を記憶するのテキスト
    remember_text = ft.Text(
        "次回以降もこの設定を記憶する",
        bgcolor=ft.colors.WHITE
    ) 
    # 記憶する、しないのラジオボタンの処理
    cg = ft.RadioGroup(
        value="記憶する",
        content=ft.Row([
            ft.Radio(value='記憶する', label="記憶する"),
            ft.Radio(value='記憶しない', label="記憶しない")
        ],
        spacing=50
        )
    )

    # テキストとラジオボタンの二つを中央に配置するためのcontainer
    center = ft.Container(
        content=ft.Column(
            controls=[remember_text,cg]
        ),
        padding=30,
        border=ft.border.all(2, ft.colors.BLACK),  # 枠線を追加
        border_radius=5,
        bgcolor=ft.colors.WHITE # 背景色
    )
    # 「Zoom会議室の設定」と「次回以降も設定を記憶するの」の二つのコンテナをRow
    center_container=ft.Row(
        controls=[zoom_text_container,center],
        spacing=20  # 要素間の基本的な間隔
    )
    
    # Zoom会議室のセキュリティ設定とオプション設定のチェックボックス============
    # テキストの処理
    t1 = ft.Text(
        "セキュリティ設定:",
        bgcolor=ft.colors.WHITE
    )
    # 待機室のチェックボックス
    c1 = ft.Checkbox(
        # label="待機室", value=get_setting_zoom()[0]
        label="待機室", 
        value=get_setting_zoom()[0]
    )
    # 参加時に認証を求めるのチェックボックス
    c2 = ft.Checkbox(label="参加時に認証を求める", value=get_setting_zoom()[1])
    # オプション設定のチェックボックス
    t2 = ft.Text("オプション設定:",bgcolor=ft.colors.WHITE)
    # 任意の時刻に参加することを参加者に許可しますのチェックボックス
    c3 = ft.Checkbox(label="任意の時刻に参加することを参加者に許可します", value=get_setting_zoom()[2])
    # 入室時に参加者をミュートにするのチェックボックス
    c4 = ft.Checkbox(label="入室時に参加者をミュートにする", value=get_setting_zoom()[3])
    # ミーティングを自動的に記録するのチェックボックス
    c5 = ft.Checkbox(label="ミーティングを自動的に記録",value=get_setting_zoom()[4], on_change=checkbox_changed)

    # ミーティングを自動的に記録するの押下後出現するラジオボタンの処理
    radio_group = ft.RadioGroup(
        value=get_setting_zoom()[5],
        content=ft.Row([
        ft.Radio(value="local", label="ローカルコンピューター上"),
        ft.Radio(value="cloud", label="クラウド内"),
        ]),
        visible=get_setting_zoom()[4] # 初期状態では非表示     
    )
    # テキストとチェックボタンを縦に並べる処理
    zoom = ft.Column(
        controls=[t1,c1,c2,t2,c3,c4]
    )
    # 「ミーティングを自動的に記録する」のチェックボックスと「ラジオボタン」を横一列に並べる処理
    zoomoption = ft.Row(
        controls = [c5,radio_group]
    )
    # Zoom会議室関係の全体を囲むコンテナ
    zm = ft.Container(
        content=ft.Column(controls=[zoom, zoomoption]), 
        padding=10,
        border=ft.border.all(2, ft.colors.BLACK),  # 一つの枠線
        border_radius=5,
        bgcolor=ft.colors.WHITE  # 背景色を白に
    )

    # 「最前列で表示または最前列ではない」の表示======
    # テキスト
    t1 = ft.Text("本自動化ツールの最前列表示（ボタンを押してください):",bgcolor=ft.colors.WHITE,visible=True)
    # Jsonファイルから記憶情報の呼び出し
    fro = get_setting_zoom()[6]
    if fro == (True):
        page.window.always_on_top = True
    else:
        page.window_always_on_top = False
    page.update()
    # ボタン処理（押下後反映）
    # 常に最前列で表示ボタンの処理
    b1 = ft.ElevatedButton(
        content=ft.Text(
            "常に最前列で表示",
            size=20
        ), 
        on_click=button_clicked,
        # visible= True,
        style=ft.ButtonStyle(
            color=ft.colors.BLACK,  # 文字色
            bgcolor=ft.colors.BLUE_300,  # 背景色
            padding=10,  # ボタン内部の余白を増やす（必要に応じて）
            shape=ft.RoundedRectangleBorder(radius=0)
        )
    )
    # 最前列ではないボタンの処理
    b2 = ft.ElevatedButton(
        content=ft.Text(
            "最前列ではない",
            size=20
        ), 
        on_click=button_clicked,
        style=ft.ButtonStyle(
            color=ft.colors.BLACK,  # 文字色
            bgcolor=ft.colors.BLUE_300,  # 背景色
            padding=10,  # ボタン内部の余白を増やす（必要に応じて）
            shape=ft.RoundedRectangleBorder(radius=0)  
        )
    )
    # テキストと二つのボタンを横一列で並べる
    teb = ft.Row(
        controls=[t1,b1,b2],
        spacing=20
    )
    # コンテナにし、枠線で外側を囲む
    tb = ft.Container(
        content=teb,
        padding=15,
        border=ft.border.all(2, ft.colors.BLACK),  # 一つの枠線
        border_radius=5,
        bgcolor=ft.colors.WHITE  # 背景色を白に
    )
    # サイボウズのログイン関係================================
    # テキスト
    t1 = ft.Text("サイボウズのログイン（初回のみ記入してください)",bgcolor=ft.colors.WHITE)
    t2 = ft.Text("ログイン名:")
    # ログイン名の入力欄
    Login_name = ft.TextField(width=250, value=get_login_data()[0])
    t3 = ft.Text("パスワード:")
    # パスワードの入力欄
    Password = ft.TextField(width=250, value=get_login_data()[1])
    # 横一列で並べる
    sac = ft.Row(
        controls=[t2,Login_name,t3,Password]
    )
    # 外側を枠線で囲む
    sc = ft.Container(
        content=ft.Column(  # contentにColumnを使う
            controls=[t1, sac]  # Columnの中にt1とsacを入れる
        ),
        padding=15,
        border=ft.border.all(2, ft.colors.BLACK),  # 一つの枠線
        border_radius=5,
        bgcolor=ft.colors.WHITE  
    )

    # 折り畳み２個分の表示・スクロール==========
    lv = ft.ListView(
        controls=[
            # 折り畳みに入っていないツールスタートボタンとサイボウズURL貼り付け欄のコンテナ
            ft.Container(content=setting_container, margin=ft.Margin(left=10,top=10,right=10,bottom=10)),
            ft.Container(content=container, margin=ft.Margin(left=10,top=10,right=10,bottom=10)),
            ft.ExpansionTile(
                title=ft.Text("オプション設定"),
                subtitle=ft.Text("スクロールして設定してください。"),
                affinity=ft.TileAffinity.LEADING,
                initially_expanded=False,
                collapsed_text_color=ft.colors.BLUE,
                text_color=ft.colors.BLUE,
                # 一個目の折り畳みの中に格納されている三つのコンテナ
                controls=[
                    ft.Container(content=center_container, margin=ft.Margin(left=10,top=10,right=10,bottom=10)),
                    ft.Container(content=zm, margin=ft.Margin(left=30,top=10,right=10,bottom=10)),
                    ft.Container(content=tb, margin=ft.Margin(left=30,top=10,right=10,bottom=10)),
                ]
            ),
            # ２個目の折り畳みの中にあるサイボウズログイン関係のコンテナ
            ft.ExpansionTile(
                title=ft.Text("サイボウズログイン"),
                subtitle=ft.Text("初回は、ログイン名とパスワードを入力してください。"),
                affinity=ft.TileAffinity.LEADING,
                initially_expanded=False,
                collapsed_text_color=ft.colors.BLUE,
                text_color=ft.colors.BLUE,
                controls=[
                    ft.Container(content=sc, margin=ft.Margin(left=30,top=10,right=10,bottom=10))
                ]
            ),

        ],
        height=page.window.height,
        expand=1
        )
    page.add(lv)
ft.app(target=main)