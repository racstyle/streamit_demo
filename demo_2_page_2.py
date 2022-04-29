import streamlit as st
import pandas as pd

def app():
    st.title("Order summary")
    
    st.header("Most recent order(s)")
    if "recent_order_table" in st.session_state:
        st.write(st.session_state["recent_order_table"])
    else:
        st.warning("Uh oh, you need to visit the first page before you can see this!")
    
    st.header("All previous orders")
    if "all_orders_table" in st.session_state:
        st.write(st.session_state["all_orders_table"])
    else:
        st.warning("Uh oh, you need to visit the first page before you can see this!")
    
    return