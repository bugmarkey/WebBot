import streamlit as st
from scrape import (scrape_website, body_content, cleared_content, split_content)
from parse import parse_with_ollama

st.title("Web Scraping AI")

url = st.text_input("Enter the URL")

if st.button("Scrap Site"):
    st.write("Scraping the site...")
    
    result = scrape_website(url)

    extracted_body = body_content(result)
    body_cleared_content = cleared_content(extracted_body)

    st.session_state.dom_content = body_cleared_content 
    
    with st.expander("View DOM Content"):
        st.text_area("DOM Content", body_cleared_content, height=350)
    
if "dom_content" in st.session_state:
    parse_description = st.text_area("Give the description")
    if st.button("Summarize"):
        if parse_description:
            st.write("Summarizing the content...")
            dom_chunks = split_content(st.session_state.dom_content)
            final_result = parse_with_ollama(dom_chunks, parse_description)
            st.write(final_result)