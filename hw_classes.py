import os
import json

list_of_ips = ["61.115.164.56", "131.136.232.245", "128.221.250.10", "56.162.8.100", "158.190.91.140"]


class IpManager:
	def __init__(self, ip_list):
		self._ip_list = ip_list

	def get_all_ips(self):
		print(self._ip_list)
		return self._ip_list

	def __ip_split(self, ip):
		return ip.split(".")

	def revert_ip(self):
		result_list = []
		for ip in self._ip_list:
			result_list.append(".".join(reversed(self.__ip_split(ip))))
		print(result_list)

	def remove_first_octet(self):
		result_list = []
		for ip in self._ip_list:
			result_list.append(".".join(self.__ip_split(ip)[1:4]))
		print(result_list)

	def show_last_octet(self):
		result_list = []
		for ip in self._ip_list:
			result_list.append(self.__ip_split(ip)[3])
		print(result_list)


ip_manage = IpManager(ip_list=list_of_ips)
ip_manage.get_all_ips()
ip_manage.revert_ip()
ip_manage.remove_first_octet()
ip_manage.show_last_octet()

# ------------- TASK 2


class FileManager:
	def __init__(self, first_file_path, second_file_path):
		self._first_file_path = first_file_path
		self._second_file_path = second_file_path

	def _file_chooser(self, which_file):
		"""helper method that make choose with which file we want work"""
		if which_file == 1:
			file_path = os.path.realpath(self._first_file_path)
		elif which_file == 2:
			file_path = os.path.realpath(self._second_file_path)
		else:
			return 'no such file'
		return file_path

	@staticmethod
	def open_file(file_path):
		"""You should define in which file to write"""
		try:
			if os.path.exists(os.path.realpath(file_path)):
				with open(file_path) as fr:
					data = json.load(fr)
				print(data)
				return data
			else:
				raise FileNotFoundError
		except json.JSONDecodeError:
			raise json.JSONDecodeError

	def write_file(self, file_path, some_info):
		"""You should define in which file to write"""
		if some_info:
			print(file_path)
			with open(file_path, 'w') as fw:
				fw.write(some_info)

	def combine_two_files(self):
		"""combine two files that is inside of object of class"""
		data1 = self.open_file(self._first_file_path)
		data2 = self.open_file(self._second_file_path)
		with open('files/compared_file', 'w') as fw:
			fw.write(json.dumps(data1, indent=4))
			fw.write(json.dumps(data2, indent=4))

	def get_relative_path(self, which_file):
		file_path = self._file_chooser(which_file)
		print(os.path.relpath(file_path))

	def get_absolute_path(self, which_file):
		file_path = self._file_chooser(which_file)
		print(os.path.abspath(file_path))


file_worker = FileManager('files/example_json_1.json', 'files/example_json_2.json')
file_worker.open_file('files/example_json_2.json')
file_worker.combine_two_files()
# file_worker.write_file('files/example_json_2.json', 'this data now will be in file 2')
file_worker.get_relative_path(1)
file_worker.get_absolute_path(1)


# ------------- TASK 3


class ConnectManager:
	def __init__(self):
		self._unit_name = None
		self._mac_address = None
		self._ip_address = None
		self._login = None
		self._password = None

	@property
	def unit_name(self):
		return self._unit_name

	@unit_name.setter
	def unit_name(self, new_unit_name):
		self._unit_name = new_unit_name

	@property
	def mac_address(self):
		return self._mac_address

	@mac_address.setter
	def mac_address(self, new_mac_address):
		self._mac_address = new_mac_address

	@property
	def ip_address(self):
		return self._ip_address

	@ip_address.setter
	def ip_address(self, new_ip_address):
		self._ip_address = new_ip_address

	@property
	def login(self):
		return self._login

	@login.setter
	def login(self, new_login):
		self._login = new_login

	@property
	def password(self):
		return self._password

	@password.setter
	def password(self, new_password):
		self._password = new_password


connector = ConnectManager()

connector.login = 'petya'
print(connector.login)

connector.password = 1111
print(connector.password)