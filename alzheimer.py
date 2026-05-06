import streamlit as st
import math

# 화면 제목과 설명
st.title("알츠하이머 위험도 자가진단")
st.write("본 모델은 수학적 모델링을 기반으로 한 스크리닝 도구입니다.")

# 사용자 입력 받기 (사이드바 또는 메인 화면)
age = st.number_input("만 나이를 입력하세요", min_value=0, max_value=120, value=65)
gender = st.radio("성별", ["남성", "여성"])
# ... (가족력, 심혈관질환, 증상 점수 등 입력창 추가)

# 결과 계산 버튼
if st.button("위험도 확인하기"):
    # 위에서 작성한 calculate_alzheimer_risk 함수 로직 적용
    # 결과 출력
    st.success(f"당신의 위험도는 {result}%입니다.")