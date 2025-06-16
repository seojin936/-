import streamlit as st

# 세션 상태 초기화
if 'game_over' not in st.session_state:
    st.session_state.game_over = False

# 게임 종료 처리
if st.session_state.game_over:
    st.write("게임이 종료되었습니다.")
    if st.button("새 게임 시작"):
        st.session_state.game_over = False
        # 추가적인 초기화 코드
else:
    # 게임 진행 중 UI
    st.write("게임 진행 중...")
    if st.button("게임 종료"):
        st.session_state.game_over = True
