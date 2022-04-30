import streamlit as st

def app():
    st.title("Streamlit + Python Resources")
    st.write("This page contains some helpful resources to help you with your Streamlit experience.")
    
    resources_cols = st.columns((5, 5))
    
    # Learn Python
    with resources_cols[0].expander("Learn Python"):
        st.write("[Interactive Python tutorial](https://www.w3schools.com/python/)")
        st.write("[REPL, a live compiler to play with Python](https://replit.com/languages/python3)")
        st.write("[Download Python](https://replit.com/languages/python3)")
        st.write("[PyPI homepage](https://pypi.org/)")
    
    # Anaconda
    with resources_cols[0].expander("Anaconda"):
        st.write("[Managing environments](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)")
        st.write("[Anaconda docs (includes conda commands)](https://docs.conda.io/projects/conda/en/latest/index.html)")
        st.write("[Anaconda GUI + CLI download](https://www.anaconda.com/products/individual)")
        st.write("[Anaconda CLI-only download](https://docs.conda.io/en/latest/miniconda.html)")
    
    # Streamlit
    with resources_cols[0].expander("Streamlit"):
        st.write("[Getting started with Streamlit](https://docs.streamlit.io/library/get-started)")
        st.write("[Streamlit cheatsheet](https://docs.streamlit.io/library/cheatsheet)")
        st.write("[Full Streamlit documentation](https://docs.streamlit.io/library/api-reference)")
        st.write("[Connect Streamlit with backend database](https://docs.streamlit.io/knowledge-base/tutorials/databases)")
        st.write("[INteractive history of Streamlit](https://docs.streamlit.io/library)")
    
    # UIC Engineering Expo
    with resources_cols[0].expander("UIC Engineering Expo"):
        st.write("[My Asianeering team's project](https://engineeringexpo.uic.edu/news-stories/caught-you-phone-handed/)")
        st.write("[UIC Engineering Expo website](https://engineeringexpo.uic.edu/)")
        st.write("[Be an Expo judge!](https://engineeringexpo.uic.edu/be-an-expo-judge/)")
    
    return