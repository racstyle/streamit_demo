import streamlit as st
import pandas as pd

def app():
    st.title("Streamlit basics")    # big title text formatting
    
    # Intro "paragraph"
    st.write("Hello, this section will cover examples of some Streamlit widgets used in this demo.")    # basic text formatting
    st.markdown("In the code, anything starting with `st` in front is called a Streamlit widget (like this *Markdown* widget!)")    # basic Markdown support
    st.write("Let's look at some examples of these Streamlit widgets that are used in this demo.")
    
    st.markdown("---")       # horizontal line
    
    # Some sample Excel data
    excel_file = pd.read_excel("example_excel_data.xlsx", sheet_name="Sheet1")  # read in Excel file via pandas library
    excel_dataframe = pd.DataFrame(excel_file)    # converting raw data into pandas dataframe to make it easy to read and manipulate in Python
    
    
    # Expander
    with st.expander("Expander"):
        st.header("Expander")
        st.write("Each of these examples are inside a widget `st.expander()` which is exactly what it sounds, a foldable component that can be expanded/closed by clicking on it, like what you just did to this one!")
        
        st.markdown("[*Documentation*](https://docs.streamlit.io/library/api-reference/layout/st.expander)")
    
    # Write
    with st.expander("Write"):
        st.header("Write")
        st.write("We will use a lot of `st.write()` in this demo.  It is used mainly for basic text but it can also be used for Markdown and even displaying tables.")
        st.write("This is `st.write()` with basic Markdown including `code`, *italic*, **bold**, and even ~strikethrough~")
        
        st.write("This is `st.write()` displaying a sample table: ", excel_dataframe)
        st.markdown("*[Sample data source](https://www.contextures.com/xlsampledata01.html#data)*")
        st.markdown("This data was read using the pandas package.")
        
        st.markdown("[*Documentation*](https://docs.streamlit.io/library/api-reference/write-magic/st.write)")
    
    # Markdown
    with st.expander("Markdown"):
        st.header("Markdown")
        st.write("The `st.markdown()` widget does the exact same as `st.write()` except all Markdown.  You can still use this widget to help you distinguish your Markdown from plain text.")
        
        st.write("You can use Markdown for inline equations such as $f(x) = x^2$ for example.")
        
        st.markdown("[*Documentation*](https://docs.streamlit.io/library/api-reference/text/st.markdown)")
    
    # Titles and headers
    with st.expander("Titles and Headers"):
        st.header("Titles and Headers")
        st.write("As the names suggests, the widgets `st.title` and `st.header` format the text to give it title and header styles, respectively.")
        
        st.title("This is a title")
        st.header("This is a header")
        st.subheader("You can also have subheaders")
        
        st.markdown("[*Title Documentation*](https://docs.streamlit.io/library/api-reference/text/st.title)")
        st.markdown("[*Header Documentation*](https://docs.streamlit.io/library/api-reference/text/st.header)")
        st.markdown("[*Subheader Documentation*](https://docs.streamlit.io/library/api-reference/text/st.subheader)")
    
    # Checkbox
    with st.expander("Checkbox"):
        st.header("Checkbox")     # header formatting
        st.write("There a lot of uses for `st.checkbox()` but one example I use a lot is showing/hiding some info in our app to not overwhelm our users with a lot of info and data.  This is where the `st.checkbox()` comes in.")
        
        st.write("Say we want to show some example Excel data.  Instead of bombarding the user with it, we can provide a checkbox the user can toggle when they are ready:")
        if st.checkbox("Show raw data"):
            st.dataframe(excel_dataframe)   # show the raw data as a dataframe table
            # st.table(excel_dataframe)       # you can also show it as a static table
            st.markdown("*[Sample data source](https://www.contextures.com/xlsampledata01.html#data)*")
            st.markdown("This data was read using the pandas package.")
        
        st.markdown("[*Checkbox Documentation*](https://docs.streamlit.io/library/api-reference/widgets/st.checkbox)")
        st.markdown("[*Dataframe Documentation*](https://docs.streamlit.io/library/api-reference/widgets/st.dataframe)")
        st.markdown("[*Table Documentation*](https://docs.streamlit.io/library/api-reference/widgets/st.table)")

    # Radio buttons
    with st.expander("Radio buttons"):
        st.header("Radio buttons")
        st.write("Similar to checkbox, we can control how much the user sees by having them select what they want by using `st.radio()`.")
        st.write("Typically used as navigation in this demo.")
        
        items_list = excel_dataframe["Item"].unique()   # this allows me to get a list of unique values in the given Excel/dataframe column
        radio_value = st.radio(label="Choose an item", options=items_list)
        st.write("You chose: ", radio_value)
        
        st.markdown("[*Documentation*](https://docs.streamlit.io/library/api-reference/widgets/st.radio)")
    
    # Select box
    with st.expander("Select box"):
        st.header("Select box")
        st.write("And similar to radio buttons, use can use a dropdown with `st.selectbox()` to choose an item from a Python list")
        
        selectbox_value = st.selectbox(label="Choose an item again", options=items_list)
        st.write("You chose: ", selectbox_value)
        
        st.markdown("[*Documentation*](https://docs.streamlit.io/library/api-reference/widgets/st.selectbox)")

    # Button
    with st.expander("Button"):
        st.header("Button")
        st.write("Button, `st.button()`, can also be used to start something in your app.  It is similar to checkbox except you will have to create your own function to toggle something back and forth.")
        
        button_clicked = st.button("Show raw data")
        if button_clicked:      # if the button was pressed, run the indented code
            st.dataframe(excel_dataframe)
        
        st.markdown("[*Documentation*](https://docs.streamlit.io/library/api-reference/widgets/st.button)")

    # Columns
    with st.expander("Formatting with columns"):
        st.header("Columns")
        st.write("Your content does not have to be limited to just one single column.  You can have responsive columns to fit more info in the app!")
        
        col1, col2 = st.columns((5, 5))
        col1.write("This is in column 1")   # this will be in column 1
        col2.write("This is in column 2")   # this will be in column 2
        col1.dataframe(excel_dataframe)     # this will be in column 1
        
        st.markdown("[*Documentation*](https://docs.streamlit.io/library/api-reference/widgets/st.columns)")

    # Dialogue boxes
    with st.expander("Dialogue boxes"):
        st.header("Dialogue boxes")
        st.write("Sometimes, we want to make sure the user sees our message.  This is where dialogue boxes come in.")
        st.write("We can also use Markdown in these widgets.")
        
        st.error("ERROR 404 *NOT **FOUND***!")
        st.warning("Heed my warning ye who lack wisdom!")
        st.info("**Fun fact:** Python can be used to make web apps via Streamlit")
        st.success("YES we did it!")
        
        st.markdown("[*Error Documentation*](https://docs.streamlit.io/library/api-reference/widgets/st.error)")
        st.markdown("[*Warning Documentation*](https://docs.streamlit.io/library/api-reference/widgets/st.warning)")
        st.markdown("[*Info Documentation*](https://docs.streamlit.io/library/api-reference/widgets/st.info)")
        st.markdown("[*Success Documentation*](https://docs.streamlit.io/library/api-reference/widgets/st.success)")

    # A note on databases (using API)
    with st.expander("A note on databases"):
        st.header("A note on databases")
        st.write("While this example uses an Excel file, you can also connect your Streamlit app with a different database via Streamlit's API (e.g. SQL databases).  See more details in this resource below:")
        st.write("https://docs.streamlit.io/library/api-reference")
        st.write("For the sake of this demo, I will only be using a static Excel file as my database.")


    st.markdown("---")
    st.write("Now that we know the basics of Streamlit, let's go to the next page to see another Streamlit example.")

    return