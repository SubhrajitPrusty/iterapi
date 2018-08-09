# iterapi
Python API to student portal of ITER

## Installation

` pip install iterapi `

## Usage

```python
import iterapi

st = iterapi.Student('regdno','password')
st.getInfo() # returns json element
st.getPhoto() # writes photo as registration_no.jpg
st.getAttendance() # returns json element

print(st.details, st.attendance)
```