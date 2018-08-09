import requests
import json

class Student(object):
	"""Student Object containing functions to retrieve various student details"""

	LOGIN_URL = "http://111.93.164.90:8282/CampusPortalSOA/login"
	STUDENTINFO_URL = "http://111.93.164.90:8282/CampusPortalSOA/studentinfo"
	STUDENTPHOTO_URL = "http://111.93.164.90:8282/CampusPortalSOA/image/studentPhoto"
	ATTENDANCE_URL = "http://111.93.164.90:8282/CampusPortalSOA/attendanceinfo"

	HEADERS = {"Content-Type" : "application/json"}

	def __init__(self, regdno, password):
		super(Student, self).__init__()
		self.regdno = regdno
		self.password = password
		self.cookies = self.login()
		self.details = None
		self.attendance = None

	def login(self):
		"""
		Logs in the student portal to retrieve cookies
		
		self.cookies

		"""
		payload = str({"username":self.regdno, "password":self.password, "MemberType":"S"})

		response = requests.post(Student.LOGIN_URL, data=payload, headers=Student.HEADERS)
		if response.status_code == 200:
			return response.cookies
		else:
			print("Cannot connect to server.")
			return None

	def getInfo(self):
		"""
		Gets studentinfo

		self.details

		"""
		response = requests.post(Student.STUDENTINFO_URL,data={},headers=Student.HEADERS, cookies=self.cookies)

		res = json.loads(response.content)
		self.details = res

	def getPhoto(self):
		""" Downloads Student Profile Picture """
		response = requests.get(Student.STUDENTPHOTO_URL, data={}, headers=Student.HEADERS, cookies=self.cookies)
		res = response.content
		with open(self.regdno+".jpg", "wb") as image:
			image.write(res)
		

	def getAttendance(self):
		"""
		Gets current Attendance 

		self.attendance

		"""
		payload = str({"registerationid": "ITERRETD1806A0000001"})
		response = requests.get(Student.ATTENDANCE_URL, data=payload, headers=Student.HEADERS, cookies=self.cookies)
		res = json.loads(response.content)
		self.attendance = res
