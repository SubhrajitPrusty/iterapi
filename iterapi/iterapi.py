import requests

class Student(object):
	"""Student Object containing functions to retrieve various student details"""

	LOGIN_URL = "http://136.233.14.3:8282/CampusPortalSOA/login"
	STUDENTINFO_URL = "http://136.233.14.3:8282/CampusPortalSOA/studentinfo"
	STUDENTPHOTO_URL = "http://136.233.14.3:8282/CampusPortalSOA/image/studentPhoto"
	STUDENTRESULT_URL = "http://136.233.14.3:8282/CampusPortalSOA/stdrst"
	RESULTDETAIL_URL = "http://136.233.14.3:8282/CampusPortalSOA/rstdtl" # styno = int(1-8) semester number
	ATTENDANCE_URL = "http://136.233.14.3:8282/CampusPortalSOA/attendanceinfo"

	HEADERS = {"Content-Type" : "application/json"}

	def __init__(self, regdno, password):
		super(Student, self).__init__()
		self.regdno = regdno
		self.password = password
		self.cookies = self.login()
		self.details = None
		self.attendance = None
		self.results = None
		self.resultDetail = dict()

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
			print("Cannot connect to server.", response)
			return None

	def getInfo(self):
		"""
		Gets studentinfo

		self.details

		"""
		response = requests.post(Student.STUDENTINFO_URL,data={},headers=Student.HEADERS, cookies=self.cookies)

		res = response.json()
		
		if response.status_code == 200:
			self.details = response.json()
			return self.details
		else:
			print("Cannot connect to server.", response)
			return None

	def getPhoto(self):
		""" Downloads Student Profile Picture """
		response = requests.get(Student.STUDENTPHOTO_URL, data={}, headers=Student.HEADERS, cookies=self.cookies)
		res = response.content

		if self.cookies:
			if response.status_code == 200:
				img_path = self.regdno+".jpg"
				with open(img_path, "wb+") as image:
					image.write(res)
					print("File written to {}".format(img_path))
					return True
		else:
			print("Cannot connect to server.", response)
			return None
		

	def getAttendance(self):
		"""
		Gets current Attendance 

		self.attendance

		"""
		payload = str({"registerationid": "ITERRETD1810A0000001"})
		response = requests.post(Student.ATTENDANCE_URL, data=payload, headers=Student.HEADERS, cookies=self.cookies)

		if response.status_code == 200:
			self.attendance = response.json()
			return self.attendance
		else:
			print("Cannot connect to server.", response)
			return None

	def getResult(self):
		"""
		Gets results

		self.result
		"""

		payload = "{}"
		response = requests.post(Student.STUDENTRESULT_URL, data=payload, headers=Student.HEADERS, cookies=self.cookies)

		if response.status_code == 200:
			self.results = response.json()
			return self.results
		else:
			print("Cannot fetch results.", response)
			return None

	def getDetailedResult(self, sem):
		"""
		Gets result details of a semester
		"""

		payload = {"styno" : str(sem)}

		response = requests.post(Student.RESULTDETAIL_URL, data=str(payload), headers=Student.HEADERS, cookies=self.cookies)
		
		if response.status_code == 200:
			self.resultDetail[sem] = response.json()
			return self.resultDetail[sem]
		else:
			print("Cannot fetch results.", response)
			return None


