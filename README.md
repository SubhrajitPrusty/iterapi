# iterapi
Python API to Student's Campus portal of ITER

[![GitHub top language][ico-lang]][link-github]
[![Licence][ico-licence]][link-pypi]
[![Latest Version][ico-version]][link-pypi]
[![Format][ico-format]][link-pypi]
[![Status][ico-status]][link-pypi]
[![Build][ico-build]][link-pypi]

## Installation

`pip install iterapi`

or

`pip3 install iterapi`

## Usage

Example

```python
from iterapi import Student

st = Student('regdno','password') # Login to the portal
st.getInfo() # returns a dictionary containing student details
st.getPhoto() # writes photo as registration_no.jpg
st.getAttendance() # returns a dictionary containing attendance
st.getResults() # returns a dictionary containing results
st.getDetailedResult(sem_no) # returns a dictionary containing details of a semester result
st.downloadSemResult(sem_no) # writes result document as registrationno_sem_no.pdf

```

[ico-lang]: https://img.shields.io/github/languages/top/SubhrajitPrusty/iterapi.svg?style=for-the-badge
[ico-version]: https://img.shields.io/pypi/v/iterapi.svg?style=for-the-badge
[ico-licence]: https://img.shields.io/pypi/l/iterapi.svg?style=for-the-badge
[ico-format]: https://img.shields.io/pypi/format/iterapi.svg?style=for-the-badge
[ico-status]: https://img.shields.io/pypi/status/iterapi.svg?style=for-the-badge
[ico-build]: https://img.shields.io/github/workflow/status/SubhrajitPrusty/iterapi/Upload%20Python%20Package?style=for-the-badge


[link-github]: https://github.com/SubhrajitPrusty/iterapi
[link-pypi]: https://pypi.org/project/iterapi

