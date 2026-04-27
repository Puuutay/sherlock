import streamlit as st
import subprocess
import sys

st.set_page_config(page_title="Sherlock OSINT Tool", layout="wide")
st.title("🕵️‍♂️ Sherlock Username Search")

username = st.text_input("I-type ang target username:", "")

if st.button("Start Investigation"):
    if username:
        st.info(f"Searching for '{username}'... Mangyaring maghintay.")
        
        # Dito natin tinatawag ang sherlock.py na nasa loob ng folder mo
        # Gagamitin natin ang sys.executable para sigurado sa python path
        command = [sys.executable, "sherlock/sherlock.py", username, "--timeout", "1"]
        
        try:
            result = subprocess.run(command, capture_output=True, text=True)
            
            if result.stdout:
                st.success("Search Results:")
                st.code(result.stdout)
            else:
                st.warning("Walang nahanap o may error sa pagtakbo.")
                
            if result.stderr:
                st.error("Error Details:")
                st.code(result.stderr)
        except Exception as e:
            st.error(f"System Error: {e}")
    else:
        st.error("Mag-input muna ng username.")
