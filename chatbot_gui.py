import streamlit as st
from template import call_openai, OPENAI_MODEL

st.set_page_config(page_title="Trợ lý AI", page_icon="🤖")
st.title("🤖 Trợ lý AI của tôi")

# Khởi tạo history trong session (giữ lại khi tương tác, mất khi F5 trang)
if "history" not in st.session_state:
    st.session_state.history = []

# Persona — sửa lại theo Câu 4.1 bạn đã viết
PERSONA = "Bạn là trợ lý học tiếng Anh, chỉ trả lời bằng tiếng Việt, giải thích ngắn gọn không quá 3 câu."

# Hiện lại các tin nhắn cũ
for msg in st.session_state.history:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Ô nhập tin nhắn mới
user_input = st.chat_input("Nhập câu hỏi...")

if user_input:
    # Hiện tin nhắn user
    with st.chat_message("user"):
        st.markdown(user_input)
    st.session_state.history.append({"role": "user", "content": user_input})

    # Gọi API và hiện phản hồi
    with st.chat_message("assistant"):
        messages = [{"role": "system", "content": PERSONA}] + st.session_state.history
        from openai import OpenAI
        import os
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        response = client.chat.completions.create(
            model=OPENAI_MODEL,
            messages=messages,
        )
        reply = response.choices[0].message.content
        st.markdown(reply)

    st.session_state.history.append({"role": "assistant", "content": reply})
    st.session_state.history = st.session_state.history[-6:]