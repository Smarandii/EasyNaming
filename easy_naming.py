import os

DESKTOP_FOLDER = os.path.join(str(os.getenv('USERPROFILE')), 'Desktop')

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
		self.mockup_files = ["preview.png"]
		self.mockup_names = []
		if color_scheme == "RGB":
			self.export_files = ["72ppi.jpg"]
			self.initial_files = ["Illustrator 2020.ai"]
		else:
			self.initial_files = ["Illustrator 2020.ai", "Project.eps"]
			self.export_files = []


class NamingHelper:
	def __init__(self, pp: ProjectProperties):
		self.pp = pp

	def create_mockups(self, mp: MockupsProperties):
		self.__mockup_names_exists(mp)
		main_folder_name = os.path.join(self.pp.project_folder, self.pp.city_name, mp.color_scheme)
		os.makedirs(main_folder_name)
		for name in mp.mockup_names:
			mockup_path = os.path.join(main_folder_name, name)
			self.__fill_mockup(mockup_path, mp.initial_f_n, mp.initial_files)
			self.__fill_mockup(mockup_path, mp.export_f_n, mp.export_files)
			self.create_empty_files(mockup_path, mp.mockup_files)

	def __fill_mockup(self, mockup_path, folder_n, files):
		mockup_path_folder_n = os.path.join(mockup_path, folder_n)
		os.makedirs(mockup_path_folder_n)
		self.create_empty_files(mockup_path_folder_n, files)
		self.__trace(mockup_path_folder_n)

	def create_empty_files(self, path, files):
		for file in files:
			self.__trace(os.path.join(path, file))
			with open(os.path.join(path, file), 'w') as fp:
				pass

	def get_mockup_names(self, colorscheme_prop: MockupsProperties):
		for i in range(colorscheme_prop.n_mockups):
			colorscheme_prop.mockup_names.append(input(f"input name for {colorscheme_prop.color_scheme} mockup №{i + 1}: "))
		return colorscheme_prop

	def __trace(self, path):
		print(path, "created")

	def __mockup_names_exists(self, mp: MockupsProperties):
		if mp.mockup_names is []:
			for i in range(mp.n_mockups):
				mp.mockup_names.append(f"mockup_{i+1}")
			return False
		else:
			return True


RGB_PROP = MockupsProperties("RGB", "Исходники", "jpg")
CMYK_PROP = MockupsProperties("CMYK", "Исходники", "Принт")


if __name__ == "__main__":
	try:
		city_name = input("input city\project name: ")
		projects_folder = input(f"input path to folder where I should create project directory or press enter to set Desktop folder {DESKTOP_FOLDER}: ")
		CMYK_PROP.n_mockups = int(input("input number of cmyk mockups: "))
		RGB_PROP.n_mockups = int(input("input number of rgb mockups: "))

		if projects_folder == "":
			projects_folder = DESKTOP_FOLDER

		pp = ProjectProperties(city_name, projects_folder, CMYK_PROP.n_mockups, RGB_PROP.n_mockups)

		nh = NamingHelper(pp)
		nh.get_mockup_names(CMYK_PROP)
		nh.get_mockup_names(RGB_PROP)
		nh.create_mockups(RGB_PROP)
		nh.create_mockups(CMYK_PROP)
		input()
	except Exception as e:
		print(e.args)
		input()