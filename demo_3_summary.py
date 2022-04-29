import streamlit as st

def app():
    st.title("Summary")
    
    st.info("Summary page")
    st.header("Values from different cases:")
    
    for case_m in range(1, st.session_state["num_cases"] + 1):
        for input_layers in range(1, st.session_state["num_layers_case_" + str(case_m)] + 1):
            st.write(st.session_state["persistent_text_case_" + str(case_m) + "_layer_" + str(input_layers)])
    