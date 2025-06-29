import streamlit as st
from src.main.services.index_data import IndexDataService
from ques_and_answer.src.main.services.rag_response import RAGResponse

index_data_service = IndexDataService()
rag_response = RAGResponse()

st.set_page_config(page_title="FAQs with RAG")

new_title = '<p style="font-family:sans-serif; color:Green; font-size: 42px;">Frequently Asked Questions powered by Bedrock, LLM, RAG 🎯</p>'
st.markdown(new_title, unsafe_allow_html=True)

if 'vector_index' not in st.session_state:
    with st.spinner("📀 Creating DB indices for Vector"):  ###spinner message
        st.session_state.vector_index = index_data_service.db_index()

input_text = st.text_area("Input text", label_visibility="collapsed")
go_button = st.button("📌GenAI is fun", type="primary")

if go_button:
    with st.spinner():
        response_content = rag_response.rag_llm_response(index=st.session_state.vector_index,
                                                question=input_text)
        st.write(response_content)