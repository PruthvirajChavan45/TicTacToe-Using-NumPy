import streamlit as st
import numpy as np

st.set_page_config(
    page_title="Tic Tac Toe",
    page_icon="🎮",
    layout="centered"
)

# ---------- CSS Styling ----------
st.markdown("""
<style>
.title {
    text-align: center;
    font-size: 42px;
    font-weight: 800;
    margin-bottom: 10px;
}

.subtitle {
    text-align: center;
    font-size: 20px;
    margin-bottom: 25px;
}

.cell button {
    height: 90px !important;
    font-size: 36px !important;
    font-weight: bold !important;
}

.status {
    text-align: center;
    font-size: 22px;
    padding: 12px;
    border-radius: 10px;
    margin-top: 20px;
}

.win {
    background-color: #d4edda;
    color: #155724;
}

.draw {
    background-color: #fff3cd;
    color: #856404;
}
</style>
""", unsafe_allow_html=True)

# ---------- Initialize State ----------
if "board" not in st.session_state:
    st.session_state.board = np.zeros((3, 3), dtype=int)
    st.session_state.current = 1
    st.session_state.winner = None


# ---------- Game Logic ----------
def check_winner(b):
    for i in range(3):
        if abs(np.sum(b[i, :])) == 3:
            return "X" if np.sum(b[i, :]) == 3 else "O"
        if abs(np.sum(b[:, i])) == 3:
            return "X" if np.sum(b[:, i]) == 3 else "O"

    diag1 = np.trace(b)
    diag2 = np.trace(np.fliplr(b))

    if abs(diag1) == 3:
        return "X" if diag1 == 3 else "O"
    if abs(diag2) == 3:
        return "X" if diag2 == 3 else "O"

    if not (b == 0).any():
        return "DRAW"

    return None


def symbol(val):
    if val == 1:
        return "❌"
    elif val == -1:
        return "⭕"
    return ""


# ---------- Header ----------
st.markdown('<div class="title">🎮 Tic Tac Toe</div>', unsafe_allow_html=True)

current_player = "❌ X" if st.session_state.current == 1 else "⭕ O"
st.markdown(
    f'<div class="subtitle">Current Turn: <b>{current_player}</b></div>',
    unsafe_allow_html=True
)

# ---------- Game Board ----------
for i in range(3):
    cols = st.columns(3)
    for j in range(3):
        with cols[j]:
            if st.button(
                symbol(st.session_state.board[i, j]),
                key=f"{i}-{j}",
                use_container_width=True,
                disabled=st.session_state.board[i, j] != 0 or st.session_state.winner is not None,
            ):
                st.session_state.board[i, j] = st.session_state.current

                result = check_winner(st.session_state.board)
                if result:
                    st.session_state.winner = result
                else:
                    st.session_state.current *= -1


# ---------- Result Display ----------
if st.session_state.winner:
    if st.session_state.winner == "DRAW":
        st.markdown(
            '<div class="status draw">🤝 Game Draw!</div>',
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f'<div class="status win">🏆 Player {st.session_state.winner} Wins!</div>',
            unsafe_allow_html=True
        )


# ---------- Restart ----------
st.markdown("---")
if st.button("🔄 Restart Game"):
    st.session_state.board = np.zeros((3, 3), dtype=int)
    st.session_state.current = 1
    st.session_state.winner = None
