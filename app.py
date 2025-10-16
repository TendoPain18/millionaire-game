import streamlit as st
import random
from classes.Questions import Questions

# Page config
st.set_page_config(page_title="Who Wants to Be a Millionaire", layout="wide")

# Custom CSS
st.markdown("""
<style>
    .main {
        background: linear-gradient(135deg, #000076 0%, #000042 100%);
    }
    .stButton > button {
        width: 100%;
        padding: 15px;
        font-size: 16px;
        font-weight: bold;
        border-radius: 8px;
        border: 2px solid white;
    }
    .question-box {
        background: #000076;
        color: white;
        padding: 20px;
        border-radius: 10px;
        font-size: 18px;
        font-weight: bold;
        margin-bottom: 30px;
    }
    .money-ladder {
        background: #1a1a1a;
        color: white;
        padding: 20px;
        border-radius: 10px;
        font-family: monospace;
        font-size: 14px;
    }
    .money-current {
        color: #00ff00;
        font-weight: bold;
    }
    .win-box {
        background: linear-gradient(135deg, #00ff00 0%, #00cc00 100%);
        color: black;
        padding: 30px;
        border-radius: 10px;
        text-align: center;
        font-size: 24px;
        font-weight: bold;
    }
    .lose-box {
        background: linear-gradient(135deg, #ff0000 0%, #cc0000 100%);
        color: white;
        padding: 30px;
        border-radius: 10px;
        text-align: center;
        font-size: 24px;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'questions_obj' not in st.session_state:
    st.session_state.questions_obj = Questions()
    st.session_state.questions_obj.readfile()
    st.session_state.current_question = 0
    st.session_state.game_state = 'playing'
    st.session_state.selected_answer = None
    st.session_state.h1_used = False
    st.session_state.h2_used = False
    st.session_state.h3_used = False

q_obj = st.session_state.questions_obj
money_levels = ['$0', '$100', '$200', '$300', '$500', '$1,000', '$2,000', '$4,000', '$8,000', '$16,000', '$32,000', '$64,000', '$125,000', '$500,000', '$1,000,000']

# Title
st.markdown("<h1 style='text-align: center; color: white;'>💰 Who Wants to Be a Millionaire 💰</h1>", unsafe_allow_html=True)

# Main game layout
if st.session_state.game_state == 'playing':
    col1, col2, col3 = st.columns([2, 1, 1])
    
    with col1:
        st.markdown(f"<div class='question-box'>{q_obj.All_Q[st.session_state.current_question]}</div>", unsafe_allow_html=True)
        
        st.markdown("### Choose your answer:")
        col_a, col_b = st.columns(2)
        with col_a:
            if st.button(f"A: {q_obj.All_A[st.session_state.current_question]}", key="btn_a"):
                st.session_state.selected_answer = q_obj.All_A[st.session_state.current_question]
                st.rerun()
        with col_b:
            if st.button(f"B: {q_obj.All_B[st.session_state.current_question]}", key="btn_b"):
                st.session_state.selected_answer = q_obj.All_B[st.session_state.current_question]
                st.rerun()
        
        col_c, col_d = st.columns(2)
        with col_c:
            if st.button(f"C: {q_obj.All_C[st.session_state.current_question]}", key="btn_c"):
                st.session_state.selected_answer = q_obj.All_C[st.session_state.current_question]
                st.rerun()
        with col_d:
            if st.button(f"D: {q_obj.All_D[st.session_state.current_question]}", key="btn_d"):
                st.session_state.selected_answer = q_obj.All_D[st.session_state.current_question]
                st.rerun()
    
    with col3:
        st.markdown("<div class='money-ladder'>", unsafe_allow_html=True)
        st.markdown("**💵 PRIZE LADDER**")
        for idx, money in enumerate(reversed(money_levels)):
            if idx == (14 - st.session_state.current_question):
                st.markdown(f"<span class='money-current'>► {money}</span>", unsafe_allow_html=True)
            else:
                st.markdown(money)
        st.markdown("</div>", unsafe_allow_html=True)
    
    # Process answer
    if st.session_state.selected_answer:
        correct_answer = q_obj.All_R[st.session_state.current_question]
        
        if st.session_state.selected_answer == correct_answer:
            if st.session_state.current_question == 14:
                st.session_state.game_state = 'won'
            else:
                st.session_state.current_question += 1
                st.session_state.selected_answer = None
        else:
            st.session_state.game_state = 'lost'
        st.rerun()
    
    # Lifelines
    st.markdown("---")
    st.markdown("### Lifelines:")
    col_h1, col_h2, col_h3 = st.columns(3)
    
    with col_h1:
        if st.button("50/50", disabled=st.session_state.h1_used, use_container_width=True):
            st.session_state.h1_used = True
            options = [
                (q_obj.All_A[st.session_state.current_question], "A"),
                (q_obj.All_B[st.session_state.current_question], "B"),
                (q_obj.All_C[st.session_state.current_question], "C"),
                (q_obj.All_D[st.session_state.current_question], "D"),
            ]
            correct = q_obj.All_R[st.session_state.current_question]
            wrong = [opt for opt in options if opt[0] != correct]
            to_remove = random.sample(wrong, 2)
            st.info(f"Eliminated: {to_remove[0][1]} and {to_remove[1][1]}")
    
    with col_h2:
        if st.button("Ask Audience", disabled=st.session_state.h2_used, use_container_width=True):
            st.session_state.h2_used = True
            correct = q_obj.All_R[st.session_state.current_question]
            st.info(f"Audience says: The answer is likely **{correct}** with 75% confidence!")
    
    with col_h3:
        if st.button("Phone a Friend", disabled=st.session_state.h3_used, use_container_width=True):
            st.session_state.h3_used = True
            correct = q_obj.All_R[st.session_state.current_question]
            st.info(f"Friend says: I think it's **{correct}**!")

elif st.session_state.game_state == 'won':
    st.markdown("<div class='win-box'>YOU WON! You are a MILLIONAIRE!</div>", unsafe_allow_html=True)
    if st.button("Play Again", use_container_width=True):
        st.session_state.questions_obj = Questions()
        st.session_state.questions_obj.readfile()
        st.session_state.current_question = 0
        st.session_state.game_state = 'playing'
        st.session_state.selected_answer = None
        st.session_state.h1_used = False
        st.session_state.h2_used = False
        st.session_state.h3_used = False
        st.rerun()

elif st.session_state.game_state == 'lost':
    money_won = money_levels[st.session_state.current_question]
    st.markdown(f"<div class='lose-box'>GAME OVER! You won: {money_won}</div>", unsafe_allow_html=True)
    if st.button("Try Again", use_container_width=True):
        st.session_state.questions_obj = Questions()
        st.session_state.questions_obj.readfile()
        st.session_state.current_question = 0
        st.session_state.game_state = 'playing'
        st.session_state.selected_answer = None
        st.session_state.h1_used = False
        st.session_state.h2_used = False
        st.session_state.h3_used = False
        st.rerun()
