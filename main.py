import streamlit as st

# 게임 상태를 세션 상태로 관리
if 'questions' not in st.session_state:
    st.session_state.questions = []
    st.session_state.answer = ''
    st.session_state.guesses = 0
    st.session_state.game_over = False

# 게임 초기화 함수
def start_game():
    st.session_state.questions = []
    st.session_state.answer = ''
    st.session_state.guesses = 0
    st.session_state.game_over = False

# 게임 종료 함수
def end_game():
    st.session_state.game_over = True

# 게임 로직
def game_logic():
    if st.session_state.game_over:
        st.write(f"게임 종료! 정답은 '{st.session_state.answer}'였습니다.")
        if st.button("새 게임 시작"):
            start_game()
        return

    st.title("스무고개 게임")
    st.write("20번의 질문을 통해 생각한 단어를 맞춰보세요!")

    question = st.text_input("질문을 입력하세요:")
    if question:
        st.session_state.questions.append(question)
        st.session_state.guesses += 1

        if st.session_state.guesses == 20:
            st.session_state.answer = "사과"  # 예시 답변
            st.session_state.game_over = True
            st.write("20번의 질문이 끝났습니다!")
            st.write(f"정답은 '{st.session_state.answer}'였습니다.")
        else:
            st.write(f"질문 {st.session_state.guesses}: {question}")

    if st.session_state.questions:
        st.write("질문 목록:")
        for i, q in enumerate(st.session_state.questions, 1):
            st.write(f"{i}. {q}")

    if st.session_state.guesses == 20:
        end_game()

if __name__ == "__main__":
    game_logic()
