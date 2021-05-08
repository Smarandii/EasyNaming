import os


class ProjectProperties:
	def __init__(self, city_name, project_folder, n_cmyk_mockups, n_rgb_mockups):
		self.city_name = city_name
		self.project_folder = project_folder
		self.n_cmyk_mockups = n_cmyk_mockups
		self.n_rgb_mockups = n_rgb_mockups


class MockupsProperties:
	def __init__(self, color_scheme, initial_f_n, export_f_n):
		self.color_scheme = color_scheme
		self.initial_f_n = initial_f_n
		self.export_f_n = export_f_n
		self.n_mockups = 0


class NamingHelper:
	def __init__(self, pp: ProjectProperties):
		self.pp = pp
		self.initial_files = []
		self.export_files = []

	def create_mockups(self, mp: MockupsProperties):
		main_folder_name = os.path.join(self.pp.project_folder, self.pp.city_name, mp.color_scheme)
		os.makedirs(main_folder_name)
		for i in range(mp.n_mockups):
			mockup_path_initial = os.path.join(main_folder_name, f"mockup_{i+1}", mp.initial_f_n)
			mockup_path_export = os.path.join(main_folder_name, f"mockup_{i+1}", mp.export_f_n)
			os.makedirs(mockup_path_initial)
			self.trace(mockup_path_initial)
			os.makedirs(mockup_path_export)
			self.trace(mockup_path_export)

	def create_empty_files_initial(self, mockup_path_initial):
		for file in self.initial_files:
			file = os.path.join(mockup_path_initial, file)
			with open(file, 'w') as file:
				pass

	def create_empty_files_export(self, mockup_path_export):
		for file in self.export_files:
			file = os.path.join(mockup_path_export, file)
			with open(file, 'w') as file:
				pass

	def trace(self, path):
		print(path, "created")


RGB_PROP = MockupsProperties("RGB", "Исходники", "jpg")
CMYK_PROP = MockupsProperties("CMYK", "Исходники", "Печать")


if __name__ == "__main__":

	city_name = input("input city\project name: ")
	projects_folder = input("input path to folder where I should create project directory: ")
	CMYK_PROP.n_mockups = int(input("input number of cmyk mockups: "))
	RGB_PROP.n_mockups = int(input("input number of rgb mockups: "))
	
	pp = ProjectProperties(city_name, projects_folder, CMYK_PROP.n_mockups, RGB_PROP.n_mockups)

	nh = NamingHelper(pp)
	nh.create_mockups(RGB_PROP)
	nh.create_mockups(CMYK_PROP)
