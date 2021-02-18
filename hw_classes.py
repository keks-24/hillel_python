import os

list_of_ips = ["61.115.164.56", "131.136.232.245", "128.221.250.10", "56.162.8.100", "158.190.91.140"]


class IpManager:
	def __init__(self, ip_list):
		self._ip_list = ip_list

	def get_all_ips(self):
		print(f"{[ip for ip in self._ip_list]}")

	def __ip_spliter(self, ip):
		return ip.split(".")

	def revert_ip(self):
		result_list = []
		for ip in self._ip_list:
			result_list.append(".".join(reversed(self.__ip_spliter(ip))))
		print(result_list)

	def remove_first_oktet(self):
		result_list = []
		for ip in self._ip_list:
			result_list.append(".".join(self.__ip_spliter(ip)[1:4]))
		print(result_list)

	def show_last_oktet(self):
		result_list = []
		for ip in self._ip_list:
			result_list.append(self.__ip_spliter(ip)[3])
		print(result_list)


ip_manage = IpManager(ip_list=list_of_ips)
ip_manage.get_all_ips()
ip_manage.revert_ip()
ip_manage.remove_first_oktet()
ip_manage.show_last_oktet()

# ------------- TASK 2


class FileManager:
	def __init__(self, file_name):
		self._file_name = os.getcwd() + '\\files\\' + file_name

	def open_file(self):
		if os.path.exists(self._file_name):
			with open(self._file_name,'r') as fr:
				data_from_file = fr.read()
			return data_from_file
		else:
			raise FileNotFoundError

	def write_file



file1 = FileManager('example_json_1.json')
file1.open_file()

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

print(connector.login)
connector.login = 'petya'
print(connector.login)

print(connector.password)
connector.password = 1111
print(connector.password)