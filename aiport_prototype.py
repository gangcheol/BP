import streamlit as st
from streamlit_option_menu import option_menu
import folium
from streamlit_folium import st_folium
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.figure_factory as ff
from PIL import Image
import emoji
import os
from urllib.parse import quote
from urllib.request import urlopen
import xml.etree.ElementTree as ET
import ssl
import requests
import jsons
import datetime
from streamlit_player import st_player
import pandas as pd
# Page setting
st.set_page_config(layout="wide", page_title="공항 이상행동 탐지 솔루션")


from IPython.display import HTML



# 사이드 바 꾸미기r
with st.sidebar: 
#logo 삽입
	st.markdown("""
	<center style='margin-top: -75px; margin-bottom: 20px;'>
		<img src='https://github.com/jayjinnie/KT-AIVLE-SCHOOL-DX-4th/blob/cae9c2e2c4a1ba3eff2b31094d5502695b38937e/21_BigProject/image/logo.png?raw=true' width=170>
	</center>
	""", unsafe_allow_html=True)

# OptionMenu 생성
	options = [
		emoji.emojize("실시간 CCTV"),
		emoji.emojize("이상행동 발생 구역 모니터링"),
		emoji.emojize("구역별 혼잡도")
		]
	selected = option_menu(menu_title="관제 서비스 선택",  # 메뉴 제목
	options=options, menu_icon="airplane")
	html = """
		<div style='
			background-color : #F0FFFF;
			width : 300px;
			padding : 13px;
			height : 60px;
			border : 2px solid;
			border-radius : 20px 20px 20px 20px;
			color : black;
			background-position: center;
			font-size : 1.2em;
			text-align : center;
			font-weight : 900;
			'>
			금일 이상행동 감지 건수 :
			<span style = "color:red">34</span>
		</div>
			"""
	st.markdown(html, unsafe_allow_html=True)
	st.markdown(" ")
	html = """
		<div style='
			background-color : #F0FFFF;
			width : 300px;
			padding : 13px;
			height : 60px;
			border : 2px solid;
			color : black;
			font-size : 1.2em;
			background-position: center;
			border-radius : 20px 20px 20px 20px;
			text-align : center;
			font-weight : 900;
			'>
			High Warning :
			<span style = "color:red">4</span>
		</div>
			"""
	st.markdown(html, unsafe_allow_html=True)
	
	st.markdown("")
	html = """
		<div style='
			background-color : #F0FFFF;
			width : 300px;
			padding : 8px;
			height : 70px;
			border : 2px solid;
			color : black;
			font-size : 1.1em;
			border-radius : 20px 20px 20px 20px;
			text-align : center;
			font-weight : 900;
			'>
			최다 알림 구역 <br>
			<span style = "color:red">2층 입국심사 B게이트</span>
		</div>
			"""
	st.markdown(html, unsafe_allow_html=True)
	
	st.markdown("")
	html = """
		<div style='
			background-color : #F0FFFF;
			width : 300px;
			padding : 8px;
			height : 70px;
			border : 2px solid;
			color : black;
			font-size : 1.1em;
			border-radius : 20px 20px 20px 20px;
			text-align : center;
			font-weight : 900;
			'>
			혼잡도 최대 구역 <br>
			<span style = "color:blue">T1 2층 입국장 E</span>
		</div>
			"""
	st.markdown(html, unsafe_allow_html=True)
# 실시간 CCTV 확인
# 실시간 CCTV 탭 선택 시 메인 화면에 탭 생성
if selected == emoji.emojize("실시간 CCTV"):

	# Markdown을 사용한 스타일링 타이틀
	st.markdown("""
		<style>
		.big-font {
			font-size:36px !important;
			font-weight: bold;
			color: #1B365C;
			margin-top: -70px;  # 텍스트 위의 여백 줄임
		}
		</style>
		""", unsafe_allow_html=True)
	st.markdown('<p class="big-font" style="color:white;">실시간 CCTV</p>', unsafe_allow_html=True)

	
	tab1, tab2, tab3, tab4 = st.tabs(["1층", "2층", "3층", "4층"])
	with tab1:        
        # 각 CCTV 위치에 해당하는 동영상 파일 경로 또는 URL
		video_file_paths = [
			os.path.abspath('video/normal1.mov'),  # CCTV 동영상 파일 경로
			os.path.abspath('video/normal2.mov'),
			os.path.abspath('video/normal3.mov'),
			os.path.abspath('video/normal4.mov'),
			os.path.abspath('video/falldown_detection.mov'),
			os.path.abspath('video/normal5.mov')
		]
        
		cctv_titles = [
			'1~3번 출입구',
			'4~6번 출입구',
			'7~9번 출입구',
			'10~12번 출입구',
			'13~14번 출입구',
			'택시 승강장'
		]
		
        # 3행 3열 그리드 생성 및 각 그리드에 동영상 삽입
		for i in range(2):  # 3행
			cols = st.columns(3)  # 각 행에 3열
			for j, col in enumerate(cols, start=1):
				with col:
					# 현재 행과 열에 따라 CCTV 번호 계산
					cctv_number = i * 3 + j
					st.subheader(cctv_titles[cctv_number - 1])
					# 각 CCTV 번호에 해당하는 동영상 재생
					st.video(video_file_paths[cctv_number - 1],start_time=0)

	with tab2:
		# 각 CCTV 위치에 해당하는 동영상 파일 경로 또는 URL
		video_file_paths = [
			os.path.abspath('video/normal5.mov'),  # CCTV 동영상 파일 경로
			os.path.abspath('video/normal6.mov'),
			os.path.abspath('video/normal7.mov'),
			os.path.abspath('video/normal8.mov'),
			os.path.abspath('video/normal9.mov'),
			os.path.abspath('video/normal10.mov')
		]
        
		cctv_titles = [
			'입국심사 A게이트',
			'입국심사 B게이트',
			'입국심사 C게이트',
			'입국심사 D게이트',
			'입국심사 E게이트',
			'입국심사 F게이트'
		]
        
        # 3행 3열 그리드 생성 및 각 그리드에 동영상 삽입
		for i in range(2):  # 3행
			cols = st.columns(3)  # 각 행에 3열
			for j, col in enumerate(cols, start=1):
				with col:
					# 현재 행과 열에 따라 CCTV 번호 계산
					cctv_number = i * 3 + j
					st.subheader(cctv_titles[cctv_number - 1])
                    # 각 CCTV 번호에 해당하는 동영상 재생
					st.video(video_file_paths[cctv_number - 1],start_time=0)

	with tab3:
        # 각 CCTV 위치에 해당하는 동영상 파일 경로 또는 URL
		video_file_paths = [
			os.path.abspath('video/normal8.mov'),  # CCTV 동영상 파일 경로
			os.path.abspath('video/normal7.mov'),
			os.path.abspath('video/normal6.mov'),
			os.path.abspath('video/normal5.mov'),
			os.path.abspath('video/normal4.mov'),
			os.path.abspath('video/normal3.mov')
		]
		
		cctv_titles = [
			'체크인 카운터 A',
			'체크인 카운터 B',
			'1번 자동출국심사대',
			'2번 자동출국심사대',
			'3번 자동출국심사대',
			'4번 자동출국심사대'
		]
			  
        # 3행 3열 그리드 생성 및 각 그리드에 동영상 삽입
		for i in range(2):  # 3행
			cols = st.columns(3)  # 각 행에 3열
			for j, col in enumerate(cols, start=1):
				with col:
                    # 현재 행과 열에 따라 CCTV 번호 계산
					cctv_number = i * 3 + j
					st.subheader(cctv_titles[cctv_number - 1])
					# 각 CCTV 번호에 해당하는 동영상 재생
					st.video(video_file_paths[cctv_number - 1],start_time=0)
    
	with tab4:
        # 각 CCTV 위치에 해당하는 동영상 파일 경로 또는 URL
		video_file_paths = [
            os.path.abspath('video/normal7.mov'),  # CCTV 동영상 파일 경로
            os.path.abspath('video/normal8.mov'),
            os.path.abspath('video/normal9.mov'),
            os.path.abspath('video/normal10.mov'),
            os.path.abspath('video/normal1.mov'),
            os.path.abspath('video/normal2.mov')
        ]
        
		cctv_titles = [
			'면세점 A구역',
			'면세점 B구역',
			'탑승구역 1~8번',
			'탑승구역 16~21번',
			'탑승구역 34~39번',
			'탑승구역 47~50번'
		]
            
        # 3행 3열 그리드 생성 및 각 그리드에 동영상 삽입
		for i in range(2):  # 3행
			cols = st.columns(3)  # 각 행에 3열
			for j, col in enumerate(cols, start=1):
				with col:
                    # 현재 행과 열에 따라 CCTV 번호 계산
					cctv_number = i * 3 + j
					st.subheader(cctv_titles[cctv_number - 1])
                    # 각 CCTV 번호에 해당하는 동영상 재생
					video_file = open(video_file_paths[cctv_number - 1], 'rb')
					video_bytes = video_file.read()
					st.video(video_bytes, start_time=2)
# 이상행동 EVENT 확인
if selected == emoji.emojize("이상행동 발생 구역 모니터링"):
    # Markdown을 사용한 스타일링 타이틀
	st.markdown("""
		<style>
		.big-font {
			font-size:36px !important;
			font-weight: bold;
			color: #1B365C;
			margin-top: -70px;  # 텍스트 위의 여백 줄임
		}
		</style>
		""", unsafe_allow_html=True)
	st.markdown('<p class="big-font" style="color:white;">이상행동 발생 구역 모니터링</p>', unsafe_allow_html=True)
        
	cols = st.columns((0.6,0.4))  # 페이지를 세로로 5:5 비율로 분할
	
	with cols[0]:  # 좌측 페이지
		# CCTV 영상 출력
		st.video("video/falldown_detection.mp4", start_time=0)

	with cols[1]:  # 우측 페이지
		html = """
		<div style='
			background-color : #F0FFFF;
			width : 600px;
			padding : 15px;
			height : 60px;
			border : 2px solid;
			border-radius : 20px 20px 20px 20px;
			color : black;
			background-position: center;
			font-size : 1.2em;
			text-align : center;
			font-weight : 900;
			'>
			이상행동 <span style = "color:red">"실신"</span>이 감지되었습니다.
		</div>
			"""
		st.markdown(html, unsafe_allow_html = True)
		html = """    
		<div style='
			background-color : #F0FFFF;
			width : 600px;
			padding : 15px;
			height : 60px;
			border : 2px solid;
			border-radius : 20px 20px 20px 20px;
			color : black;
			background-position: center;
			font-size : 1.2em;
			text-align : center;
			font-weight : 900;
			'>
			상황 발생 위치 :  <span style = "color:red">"T1 1층 택시 승강장"</span>
		</div>
			"""
		st.markdown(html, unsafe_allow_html = True)
		
		html = """
		<div style='
			background-color : #F0FFFF;
			width : 600px;
			padding : 15px;
			height : 60px;
			border : 2px solid;
			border-radius : 20px 20px 20px 20px;
			color : black;
			background-position: center;
			font-size : 1.2em;
			text-align : center;
			font-weight : 900;
			'>
			해당 구역 배치 요원 수 : 총 3인
		</div>
			"""
		st.markdown(html, unsafe_allow_html = True)
		st.markdown(" ")
		st.image("이미지3.png", width = 620)
		
	data = pd.read_csv("data.csv")
	tidy_data = data.groupby(["이상행동 유형","상황 발생 위치"],as_index = False)[["사건 관련 인원 수"]].sum()
	cols = st.columns((0.6,0.4))
	with cols[1] :
		t1, t2, t3, t4, t5, t6 ,t7, t8 = st.tabs(["page1", "page2", "page3", "page4","page5","page6","page7","page8"])
	
		with t1 :
			html = data.iloc[0:5,].to_html(justify = "center",index=False)
			st.markdown(html, unsafe_allow_html = True)
		with t2 :
			html = data.iloc[5:10,].to_html(justify = "center",index=False)
			st.markdown(html, unsafe_allow_html = True)
		with t3 :
			html = data.iloc[10:15,].to_html(justify = "center",index=False)
			st.markdown(html, unsafe_allow_html = True)
		with t4 :
			html = data.iloc[15:20,].to_html(justify = "center",index=False)
			st.markdown(html, unsafe_allow_html = True)
		with t5 :
			html = data.iloc[20:25,].to_html(justify = "center",index=False)
			st.markdown(html, unsafe_allow_html = True)
		with t6 :
			html = data.iloc[25:30,].to_html(justify = "center",index=False)
			st.markdown(html, unsafe_allow_html = True)
		with t7 :
			html = data.iloc[30:35,].to_html(justify = "center",index=False)
			st.markdown(html, unsafe_allow_html = True)
		with t8 :
			html = data.iloc[35:40,].to_html(justify = "center",index=False)
			st.markdown(html, unsafe_allow_html = True)
	
	with cols[0] :
		fig = px.bar(tidy_data, x = "이상행동 유형", y="사건 관련 인원 수",
					 color = "상황 발생 위치", width = 800, title = "유형 & 위치 별 사건 관련 인원 수")
		fig.update_layout(showlegend = False, title_x = 0.4)
		st.plotly_chart(fig)
		
# 혼잡도 확인
if selected == emoji.emojize("구역별 혼잡도"):
    # 승객 혼잡도 API 로드        
	context=ssl.create_default_context()
	context.set_ciphers('DEFAULT')
	key = 'udvJG%2FCmvBCOdsMRK4RToVX2Xn90wTACwv6QfY2dYMzu1i5X2aTm9x2LbntK0RVaL2cfQ9GigHr1goleScrEUQ%3D%3D'
	url = 'http://apis.data.go.kr/B551177/PassengerNoticeKR/getfPassengerNoticeIKR?serviceKey='+key+'&selectdate=0&type=json'
	response = requests.get(url)
	result = response.content.decode("utf-8")
	json = jsons.loads(result)['response']['body']['items']
	data = pd.DataFrame(json)
	data.columns = ['일자', '시간대', 'T1 입국장 동편(A,B)', 'T1 입국장 서편(E,F)', 'T1 입국심사(C)', 'T1 입국심사(D)', 'T1 입국장 합계', 
					'T1 출국장1,2', 'T1 출국장3', 'T1 출국장4', 'T1 출국장5,6', 'T1 출국장 합계', 
					'T2 입국장 1', 'T2 입국장 2', 'T2 입국장 합계',
					'T2 출국장 1', 'T2 출국장 2', 'T2 출국장 합계']
    
    # '합계'를 가지고 있는 행을 제거
	data = data[data['일자'] != '합계']
	
    # 데이터 형 변환
	data['일자'] = pd.to_datetime(data['일자'], format='%Y%m%d')

    # 나머지 컬럼들을 float으로 변환
	float_columns = ['T1 입국장 동편(A,B)', 'T1 입국장 서편(E,F)', 'T1 입국심사(C)', 'T1 입국심사(D)', 'T1 입국장 합계',
						'T1 출국장1,2', 'T1 출국장3', 'T1 출국장4', 'T1 출국장5,6', 'T1 출국장 합계', 'T2 입국장 1', 'T2 입국장 2',
					 'T2 입국장 합계', 'T2 출국장 1', 'T2 출국장 2', 'T2 출국장 합계']
	data[float_columns] = data[float_columns].astype(float)

	st.markdown("""
		<style>
		.big-font {
			font-size:36px !important;
			font-weight: bold;
			color: #1B365C;
			margin-top: -70px;  # 텍스트 위의 여백 줄임
		}
		</style>
		""", unsafe_allow_html=True)
	st.markdown('<p class="big-font" style="color:white;">시간대별 공항 내 승객 혼잡도 현황</p>', unsafe_allow_html=True)

    # 필터 버튼 생성
	selected_column = st.selectbox("구역 선택", ['T1 입국장 합계', 'T1 출국장 합계', 'T2 입국장 합계', 'T2 출국장 합계'])

    # 데이터프레임으로부터 시간대별 합계 데이터 추출
	sumset_data = data.groupby('시간대').mean()[['T1 입국장 합계', 'T1 출국장 합계', 'T2 입국장 합계', 'T2 출국장 합계']].reset_index()

    # 시각화
	fig = px.bar(sumset_data, x='시간대', y=selected_column,
                 labels={'value': '승객 총합'},
                 title='시간대별 공항 내 승객 혼잡도 현황')
    # 결과 출력
	st.plotly_chart(fig)
	data = pd.read_csv("혼잡도.csv")
    # 필터 버튼 생성 (T1, T2 선택)
	selected_terminal = st.selectbox("터미널을 선택하세요", ['T1 입국장', 'T1 출국장', 'T2 입국장', 'T2 출국장'])

	def custom_style(value):
		
		if value <= 7000 :
			return  'background-color: grey'
		if 7000 <value <= 7600 :
			return 'background-color: blue'
		elif 7600 < value <= 8200 :
			return 'background-color: pink'
		elif 8200 <value <= 8600 :
			return 'background-color: orange'
		else :
			return 'background-color: red'
	
	def custom_style2(value):
		
		if value <= 3200 :
			return 'background-color: grey'
		if 3200 <value <= 3500 :
			return 'background-color: blue'
		elif 3500 < value <= 3800 :
			return 'background-color: pink'
		elif 3800 <value <= 4000 :
			return 'background-color: orange'
		else :
			return 'background-color: red'
	columns = ["(A,B)", "C", "D", "(E,F)"]
	
	
	if selected_terminal == "T1 입국장":
			t1,t2,t3 = st.tabs(["page1","page2","page3"])
			
			with t1 : 
				df = data.loc[data.location == selected_terminal,
							  ["시간대",'(A,B)', 'C', 'D', '(E,F)']].set_index("시간대").T
				df = df.iloc[:,0:8]
				df = df.style.applymap(custom_style)
				#st.dataframe(df)
				df = df.to_html(justify = "center",index=False)
				html = f"""
					<div style='
					color : white;
					background-position: center;
					font-size : 1.0em;
					text-align : center;
					font-weight : 900;
					'>
					{df} 
					"""
				st.markdown(html, unsafe_allow_html = True)
			with t2 : 
				df = data.loc[data.location == selected_terminal,
							  ["시간대",'(A,B)', 'C', 'D', '(E,F)']].set_index("시간대").T
				df = df.iloc[:,8:16]
				df = df.style.applymap(custom_style)
				#st.dataframe(df)
				df = df.to_html(justify = "center",index=False)
				html = f"""
					<div style='
					color : white;
					background-position: center;
					font-size : 1.0em;
					text-align : center;
					font-weight : 900;
					'>
					{df} 
					"""
				st.markdown(html, unsafe_allow_html = True)
			with t3 : 
				df = data.loc[data.location == selected_terminal,
							  ["시간대",'(A,B)', 'C', 'D', '(E,F)']].set_index("시간대").T
				df = df.iloc[:,16:24]
				df = df.style.applymap(custom_style)
				#st.dataframe(df)
				df = df.to_html(justify = "center",index=False)
				html = f"""
					<div style='
					color : white;
					background-position: center;
					font-size : 1.0em;
					text-align : center;
					font-weight : 900;
					'>
					{df} 
					"""
				st.markdown(html, unsafe_allow_html = True)
	
	elif selected_terminal == "T1 출국장":
			t1,t2,t3 = st.tabs(["page1","page2","page3"])
			
			with t1 : 
				df = data.loc[data.location == selected_terminal,
							  ["시간대",'(A,B)', 'C', 'D', '(E,F)']].set_index("시간대").T
				df = df.iloc[:,0:8]
				df = df.style.applymap(custom_style)
				#st.dataframe(df)
				df = df.to_html(justify = "center",index=False)
				html = f"""
					<div style='
					color : white;
					background-position: center;
					font-size : 1.0em;
					text-align : center;
					font-weight : 900;
					'>
					{df} 
					"""
				st.markdown(html, unsafe_allow_html = True)
			with t2 : 
				df = data.loc[data.location == selected_terminal,
							  ["시간대",'(A,B)', 'C', 'D', '(E,F)']].set_index("시간대").T
				df = df.iloc[:,8:16]
				df = df.style.applymap(custom_style)
				#st.dataframe(df)
				df = df.to_html(justify = "center",index=False)
				html = f"""
					<div style='
					color : white;
					background-position: center;
					font-size : 1.0em;
					text-align : center;
					font-weight : 900;
					'>
					{df} 
					"""
				st.markdown(html, unsafe_allow_html = True)
			with t3 : 
				df = data.loc[data.location == selected_terminal,
							  ["시간대",'(A,B)', 'C', 'D', '(E,F)']].set_index("시간대").T
				df = df.iloc[:,16:24]
				df = df.style.applymap(custom_style)
				#st.dataframe(df)
				df = df.to_html(justify = "center",index=False)
				html = f"""
					<div style='
					color : white;
					background-position: center;
					font-size : 1.0em;
					text-align : center;
					font-weight : 900;
					'>
					{df} 
					"""
				st.markdown(html, unsafe_allow_html = True)
	
	elif selected_terminal == "T2 입국장":
			t1,t2,t3 = st.tabs(["page1","page2","page3"])
			
			with t1 : 
				df = data.loc[data.location == selected_terminal,
							  ["시간대",'(A,B)', 'C', 'D', '(E,F)']].set_index("시간대").T
				df = df.iloc[:,0:8]
				df = df.style.applymap(custom_style2)
				#st.dataframe(df)
				df = df.to_html(justify = "center",index=False)
				html = f"""
					<div style='
					color : white;
					background-position: center;
					font-size : 1.0em;
					text-align : center;
					font-weight : 900;
					'>
					{df} 
					"""
				st.markdown(html, unsafe_allow_html = True)
			with t2 : 
				df = data.loc[data.location == selected_terminal,
							  ["시간대",'(A,B)', 'C', 'D', '(E,F)']].set_index("시간대").T
				df = df.iloc[:,8:16]
				df = df.style.applymap(custom_style)
				#st.dataframe(df)
				df = df.to_html(justify = "center",index=False)
				html = f"""
					<div style='
					color : white;
					background-position: center;
					font-size : 1.0em;
					text-align : center;
					font-weight : 900;
					'>
					{df} 
					"""
				st.markdown(html, unsafe_allow_html = True)
			with t3 : 
				df = data.loc[data.location == selected_terminal,
							  ["시간대",'(A,B)', 'C', 'D', '(E,F)']].set_index("시간대").T
				df = df.iloc[:,16:24]
				df = df.style.applymap(custom_style)
				#st.dataframe(df)
				df = df.to_html(justify = "center",index=False)
				html = f"""
					<div style='
					color : white;
					background-position: center;
					font-size : 1.0em;
					text-align : center;
					font-weight : 900;
					'>
					{df} 
					"""
				st.markdown(html, unsafe_allow_html = True)
			
	else:
			t1,t2,t3 = st.tabs(["page1","page2","page3"])
			
			with t1 : 
				df = data.loc[data.location == "T2 출국장",
							  ["시간대",'(A,B)', 'C', 'D', '(E,F)']].set_index("시간대").T
				df = df.iloc[:,0:8]
				df = df.style.applymap(custom_style2)
				#st.dataframe(df)
				df = df.to_html(justify = "center",index=False)
				html = f"""
					<div style='
					color : white;
					background-position: center;
					font-size : 1.0em;
					text-align : center;
					font-weight : 900;
					'>
					{df} 
					"""
				st.markdown(html, unsafe_allow_html = True)
			with t2 : 
				df = data.loc[data.location == selected_terminal,
							  ["시간대",'(A,B)', 'C', 'D', '(E,F)']].set_index("시간대").T
				df = df.iloc[:,8:16]
				df = df.style.applymap(custom_style)
				#st.dataframe(df)
				df = df.to_html(justify = "center",index=False)
				html = f"""
					<div style='
					color : white;
					background-position: center;
					font-size : 1.0em;
					text-align : center;
					font-weight : 900;
					'>
					{df} 
					"""
				st.markdown(html, unsafe_allow_html = True)
			with t3 : 
				df = data.loc[data.location == selected_terminal,
							  ["시간대",'(A,B)', 'C', 'D', '(E,F)']].set_index("시간대").T
				df = df.iloc[:,16:24]
				df = df.style.applymap(custom_style)
				#st.dataframe(df)
				df = df.to_html(justify = "center",index=False)
				html = f"""
					<div style='
					color : white;
					background-position: center;
					font-size : 1.0em;
					text-align : center;
					font-weight : 900;
					'>
					{df} 
					"""
				st.markdown(html, unsafe_allow_html = True)
	st.markdown("----------")
	st.markdown("### 색상구분")
	df=  pd.read_csv("색깔구분.csv")
	
	def colors(x) :
		return f"background : {x}"
	
	df = df.style.applymap(colors).to_html(justify = "center", index = False)
	html = f"""
			<div style='
			color : white;
			background-position: center;
			font-size : 1.0em;
			text-align : center;
			font-weight : 900;
			'>
			{df} 
			"""
	st.markdown(html, unsafe_allow_html = True)
