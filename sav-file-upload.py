import streamlit as st
import pandas as pd

#Following is the code
file = st.file_uploader("Please choose a file")

if file is not None:
  #To read file as bytes

  bytes_data = file.getvalue()

  st.write(bytes_data)



# #To convert to a string based IO:

# stringio = StringIO(file.getvalue().decode("latin1")) 

# st.write(stringio)



# #To read file as string:

# string_data = stringio.read()

# st.write(string_data)



# #Can be used wherever a "file-like" object is accepted:

# df= pd.read_spss(file)#To read file as bytes:

# bytes_data = file.getvalue()

# st.write(bytes_data)



# #To convert to a string based IO:
# #(when i tried utf-8 i got can't convert utf-8 at a axx position. so i changed it to latin1 but now i am getting above metioned error)
# stringio = StringIO(file.getvalue().decode("latin1")) 

# st.write(stringio)



# #To read file as string:

# string_data = stringio.read()

# st.write(string_data)



# #Can be used wherever a "file-like" object is accepted:

# df= pd.read_spss(file)
