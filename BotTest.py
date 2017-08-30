# -*- coding: utf-8 -*-
from chatterbot import ChatBot
from time import localtime, strftime
from shutil import copyfile
import os, errno
from chatterbot.trainers import ChatterBotCorpusTrainer
from TextProcessor.LabeledCaseProcessor import LabeledCaseProcessor

# Uncomment the following lines to enable verbose logging
import logging

# logging.basicConfig(level=logging.INFO)
# logging.basicConfig(level=logging.DEBUG)

bot = ChatBot(
	"NoteBot",
	storage_adapter="chatterbot.storage.SQLStorageAdapter",
	database_uri="sqlite:///2003database.db",
	logic_adapters=[
		{
			'import_path': 'chatterbot.logic.BestMatch'
		},
		{
			'import_path'     : 'chatterbot.logic.LowConfidenceAdapter',
			'threshold'       : 0.25,
			'default_response': 'What?'
		},
	],
	input_adapter="chatterbot.input.VariableInputTypeAdapter",
	output_adapter="chatterbot.output.OutputAdapter",
)
bot.set_trainer(ChatterBotCorpusTrainer)
# bot.train("output.out")
bot.read_only = True

# Uncommenting the following lines to make tests and produce test results
time_folder = strftime("%Y-%m-%d_%H-%M-%S", localtime())
TEST_INPUT_PATH = 'output\\test_2003.txt'
TEST_RESULT_FOLDER = 'TestResults\\' + time_folder
TEST_RESULT_FILE = TEST_RESULT_FOLDER + '\\TestResult.txt'

if not os.path.exists(TEST_RESULT_FOLDER):
	os.makedirs(TEST_RESULT_FOLDER)

input_file_name = TEST_INPUT_PATH
if TEST_INPUT_PATH.rfind('\\') != -1:
	input_file_name = TEST_INPUT_PATH[TEST_INPUT_PATH.rfind('\\'):]

copyfile(TEST_INPUT_PATH, TEST_RESULT_FOLDER + '\\' + input_file_name)

test_result_str = ''
tmp_str = ''

lcp = LabeledCaseProcessor('INFO')
cu_list = lcp.readTestFile(TEST_INPUT_PATH)

correct = 0
incorrect = 0

for idx, cu in enumerate(cu_list):
	input = cu.text
	factor = cu.factor
	output = bot.get_response(input)

	if factor == output.text:
		correct += 1
		tmp_str = "第" + str(idx + 1) + "条回答正确！\n"
		print(tmp_str)
		test_result_str += tmp_str
	else:
		incorrect += 1
		tmp_str = '!' * 100 + '\n' \
		          + '第' + str(idx + 1) + '条回答错误\n' \
		          + '原文： ' + input + '\n' \
		          + '应输出： ' + factor + '\n' \
		          + '实际输出： ' + output.text + '\n' \
		          + '!' * 100 + '\n'

		print(tmp_str)
		test_result_str += tmp_str

total = correct + incorrect
percent = correct / total * 100
tmp_str = '\n\n' + '=' * 100 + '\n'\
          + '共计测试数量：' + str(total) \
          + ' 正确数量：' + str(	correct) \
          + ' 错误数量：' + str(incorrect) \
          + ' 正确率:' + str(percent) + '%' + '\n'\
          + '=' * 100

print(tmp_str)
test_result_str += tmp_str

with open(TEST_RESULT_FILE, encoding='utf-8', mode='w') as f:
	f.write(test_result_str)

# The following loop will execute each time the user enters input
# while True:
#     try:
#         # We pass None to this method because the parameter
#         # is not used by the TerminalAdapter
#         input = "及承担本案诉讼费用"
#         bot_input = bot.get_response(input)
#         print(bot_input)
#
#     # Press ctrl-c or ctrl-d on the keyboard to exit
#     except (KeyboardInterrupt, EOFError, SystemExit):
#         break
