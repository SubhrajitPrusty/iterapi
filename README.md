# iterapi
Python API to Student's Campus portal of ITER

## Installation

Open your terminal and type `pip install iterapi` or `pip3 install iterapi`

## Usage

Type following command in console to

```python
# Imports the library
import iterapi 

st = iterapi.Student('regdno','password') # Login to the portal
st.getInfo() # returns json element
st.getPhoto() # writes photo as registration_no.jpg
st.getAttendance() # returns json element

print(st.details, st.attendance)  # Print student details and attendance on console
```
