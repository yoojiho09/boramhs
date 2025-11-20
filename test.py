import streamlit as st

st.set_page_config(page_title="오늘의 기분", layout="centered")

st.title("😊 오늘의 기분은 어떤가요?")

# 기분 선택
mood = st.selectbox(
    "기분을 선택하세요:",
    ["😊 행복해요", "😐 그냥 그래요", "😢 슬퍼요", "😡 화나요", "🤩 신나요"]
)

# 기분별 배경색
colors = {
    "😊 행복해요": "#FFE066",   # 노랑
    "😐 그냥 그래요": "#D3D3D3", # 회색
    "😢 슬퍼요": "#A7C6ED",     # 파랑
    "😡 화나요": "#FF6B6B",     # 빨강
    "🤩 신나요": "#B5E48C"      # 연두
}

bg_color = colors[mood]

# ✨ Streamlit main container 배경 변경 (버전 상관없이 안정적)
st.markdown(
    f"""
    <style>
        [data-testid="stAppViewContainer"] {{
            background-color: {bg_color};
        }}
    </style>
    """,
    unsafe_allow_html=True
)

st.write(f"현재 기분: **{mood}**")
