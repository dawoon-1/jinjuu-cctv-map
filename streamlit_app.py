import streamlit as st
import pandas as pd

# 데이터 불러오기
data = pd.read_csv("경상남도 진주시_CCTV위치정보_20250501.csv")

# 지도 출력
st.title("진주시 CCTV 지도")
st.map(data[['위도', '경도']])
