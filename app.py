import streamlit as st

st.title("Hello Aayush")
st.header("Welcome to Data Science")
st.subheader("Start Code")
st.text("Streamlit framwork for deployment")

st.markdown("Hi")
st.markdown("###### Hi")

st.success("Data is submitted")
st.warning("Warning")
st.error("Error")
st.info("Information")
st.exception(ZeroDivisionError("Error : Divisible by 0"))
st.help(ZeroDivisionError)

st.write("range(1,10)")
st.write(range(1,10))

st.code('x = 10\n'
        'for i in range(x):\n'
        '\tprint(i)')

st.checkbox("Male")
if(st.checkbox("Adult")):
    st.write("You'r an adult")

st.radio('Select :', ('Male','Female','Other'))

st.selectbox("Data Science : ", ['Data analytics', 'Web scrapping' , 'Deep learning', 'Image Processing'])

st.multiselect ("Data Science : ", ['Data analytics', 'Web scrapping' , 'Deep learning', 'Image Processing'])

st.button("Submit")

st.subheader("Slider :-")
st.slider('select the level',1,10,step = 1)

st.text_input("Name : ")
st.text_area("Write something : ")
st.number_input("Enter the number : ")
st.date_input("Date : ")
st.time_input("Time : ")