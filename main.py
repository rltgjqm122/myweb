import streamlit as st

과목 = st.selectbox("과목을 선택하세요",
                    ["확률과 통계",
                     "미분과 적분",
                     "기하와 벡터"])
st.subheader(f"당신이 선택한 과목은 {과목}입니다.")









짜장면 = st.checkbox("짜장면5000원")
짬뽕 = st.checkbox("짬뽕7000원")
탕수육 = st.checkbox("탕수육15000원")
가격 = 0
if 짜장면:
    가격+=5000
if 짬뽕:
    가격+=7000
if 탕수육:
    가격+=15000
st.subheader(f"가격은 {가격}입니다.")
    

check = st.checkbox("탕수육")
if check:
    st.write("선택한 음식의 가격은 원 입니다.")

버튼 = st.button("버튼")
if 버튼:
    st.write("버튼을 눌렀습니다")


st.title("🎂Title")
st.header("header")
st.subheader("Subheader")
st.markdown("우리 함께 **스트림릿**을 :red[배워]봅시다!!!")
st.write("우리 함께 **스트림릿**을 :ㄱㄷㅇ[배워]봅시다!!!")




