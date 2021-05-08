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
		self.mockup_files = ["Техническое задание.pdf", "preview.png"]
		if color_scheme == "RGB":
			self.export_files = ["72ppi.jpg", "300ppi.jpg"]
			self.initial_files = ["Illustrator 2020.ai", "Illustrator 10.ai", "Project.eps"]
		else:
			self.initial_files = ["Illustrator 2020.ai", "Illustrator 10.ai", "Project.eps"]
			self.export_files = ["72ppi lzw.tiff", "300ppi lzw.tiff"]


class NamingHelper:
	def __init__(self, pp: ProjectProperties):
		self.pp = pp

	def create_mockups(self, mp: MockupsProperties):
		main_folder_name = os.path.join(self.pp.project_folder, self.pp.city_name, mp.color_scheme)
		os.makedirs(main_folder_name)
		for i in range(mp.n_mockups):
			mockup_path = os.path.join(main_folder_name, f"mockup_{i+1}")
			self.fill_mockup(mockup_path, mp.initial_f_n, mp.initial_files)
			self.fill_mockup(mockup_path, mp.export_f_n, mp.export_files)
			self.create_empty_files(mockup_path, mp.mockup_files)

	def fill_mockup(self, mockup_path, folder_n, files):
		mockup_path_folder_n = os.path.join(mockup_path, folder_n)
		os.makedirs(mockup_path_folder_n)
		self.create_empty_files(mockup_path_folder_n, files)
		self.trace(mockup_path_folder_n)

	def create_empty_files(self, path, files):
		for file in files:
			self.trace(os.path.join(path, file))
			with open(os.path.join(path, file), 'w') as fp:
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
