from TextProcessor.LawCase import LawCase
from TextProcessor.ContentUnit import ContentUnit
from TextProcessor.ContentUnit import NoKeyFactorException


class LabeledCaseProcessor:
	def __init__(self, debug_level):
		self.debug_level = debug_level

	def process(self, input_file, yml_file, test_file, train_ratio):
		case_str_list = self.readfile2casestr(input_file)
		case_list = []
		for idx, line in enumerate(case_str_list):
			case = self.buildLawCase(line)
			if case:
				case_list.append(case)

		completeListSize = len(case_list)

		ratio = train_ratio
		if train_ratio > 1:
			ratio = 1
		if train_ratio < 0:
			ratio = 0

		trainListSize = int(completeListSize * ratio)
		train_list = case_list[0:trainListSize]
		test_list = case_list[trainListSize:]
		self.writeYmlFile(yml_file, train_list)
		self.writeTestFile(test_file, test_list)

	def buildLawCase(self, content):
		content_str = str(content)
		lawcase_id = 0
		if content_str.find('【--') != -1 and content_str.find('--】') != -1:
			start_idx = str(content).find('【--') + len('【--')
			end_idx = str(content).index('--】')
			lawcase_id = str(content)[start_idx:end_idx]
		# print(lawcase_id)
		else:
			return None

		if content_str.find('[原告诉称]') == -1:
			if self.debug_level == 'DEBUG':
				print("This case does not have [原告诉称] field: " + lawcase_id)
			return None

		lawcase = LawCase(lawcase_id)
		start_idx = content_str.find('[原告诉称]') + len('[原告诉称]')
		end_idx = content_str.find('[', start_idx)
		accuse_str = content_str[start_idx:end_idx]

		start_idx = 0
		end_idx = 0
		error_note = False
		cu_list = []

		start_idx = accuse_str.find('【', end_idx)
		while start_idx != -1:
			start_idx += 1
			end_idx = accuse_str.find('】', start_idx)
			chunck = accuse_str[start_idx:end_idx]
			end_idx += 1

			idx = chunck.find('：')
			if idx != -1:
				factor = chunck[0:idx]
				description = chunck[idx + 1:]
				try:
					cu = ContentUnit(factor, description)
					cu_list.append(cu)
				except NoKeyFactorException:
					if self.debug_level == 'DEBUG':
						print("Key factor " + factor + " not found!")

					# print(factor)
					# print(description)
			else:
				error_note = True

			start_idx = accuse_str.find('【', end_idx)

		lawcase.content = cu_list
		return lawcase

	def readfile2casestr(self, input_file):
		with open(input_file, encoding='utf-8') as f:
			content = f.readlines()

		case_str_list = []
		case_str = ''
		for idx, line in enumerate(content):
			if (line.startswith('【--') and not case_str == '') or idx == len(
				content) - 1:
				case_str_list.append(case_str)
				case_str = ''
			case_str += line
		return case_str_list

	def writeYmlFile(self, output_file, caseList):
		with open(output_file, encoding='utf-8', mode='w') as f:
			f.write("categories:\n")
			f.write("- CaseStudy\n")
			f.write("conversations:\n")
			for idx, case in enumerate(caseList):
				cu_list = case.content
				for index, cu in enumerate(cu_list):
					f.write("- - " + cu.text + "\n")
					f.write("  - " + cu.factor + "\n")

	def writeTestFile(self, test_file, caseList):
		with open(test_file, encoding='utf-8', mode='w') as f:
			f.write("--------LABEL TEST----------\n")
			for idx, case in enumerate(caseList):
				cu_list = case.content
				for index, cu in enumerate(cu_list):
					f.write("[Question]" + cu.text + "\n")
					f.write("[Answer]" + cu.factor + "\n")

	def readTestFile(self, test_file):
		with open(test_file, encoding='utf-8', mode='r') as f:
			content = f.readlines()

		cu_list = []
		text = ''
		factor = ''
		for idx, line in enumerate(content):
			if line.startswith('[Question]') or line.startswith('[Answer]'):
				if line.startswith('[Question]'):
					text = line[len('[Question]'):-1]
				if line.startswith(('[Answer]')):
					factor = line[len('[Answer]'):-1]
					cu = ContentUnit(factor, text)
					cu_list.append(cu)

		return cu_list
