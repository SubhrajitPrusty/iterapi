# iterapi
Python API to Student's Campus portal of ITER

[![GitHub top language][ico-lang]][link-github]
[![Licence][ico-licence]][link-pypi]
[![Latest Version][ico-version]][link-pypi]
[![Format][ico-format]][link-pypi]
[![Status][ico-status]][link-pypi]

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
st.getResults() # returns results
st.getDetailedResult(sem_no) # return details of a semester result

print(st.details, st.attendance)  # Print student details and attendance on console
```

[ico-lang]: https://img.shields.io/github/languages/top/SubhrajitPrusty/iterapi.svg?style=for-the-badge
[ico-version]: https://img.shields.io/pypi/v/iterapi.svg?style=for-the-badge
[ico-licence]: https://img.shields.io/pypi/l/iterapi.svg?style=for-the-badge
[ico-format]: https://img.shields.io/pypi/format/iterapi.svg?style=for-the-badge
[ico-status]: https://img.shields.io/pypi/status/iterapi.svg?style=for-the-badge

[link-github]: https://github.com/SubhrajitPrusty/iterapi
[link-pypi]: https://pypi.org/project/iterapi

