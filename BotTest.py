# -*- coding: utf-8 -*-
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from TextProcessor.LabeledCaseProcessor import LabeledCaseProcessor

# Uncomment the following lines to enable verbose logging
import logging
# logging.basicConfig(level=logging.INFO)
# logging.basicConfig(level=logging.DEBUG)

bot = ChatBot(
	"NoteBot",
	storage_adapter="chatterbot.storage.SQLStorageAdapter",
	database_uri="sqlite:///testdatabase.db",
	logic_adapters=[
		{
			'import_path': 'chatterbot.logic.BestMatch'
		},
		{
			'import_path': 'chatterbot.logic.LowConfidenceAdapter',
			'threshold': 0.25,
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
TEST_PATH = 'output\\test_6818.txt'
lcp = LabeledCaseProcessor('INFO')
cu_list = lcp.readTestFile(TEST_PATH)

correct = 0
incorrect = 0

for idx, cu in enumerate(cu_list):
  input = cu.text
  factor = cu.factor
  output = bot.get_response(input)

  if factor == output.text:
    correct += 1
    print("第" + str(idx + 1) + "条回答正确！")
  else:
    incorrect += 1
    print("======================================")
    print("第" + str(idx + 1) + "条回答错误")
    print("原文： " + input)
    print("应输出： " + factor)
    print("实际输出： " + output.text)
    print("======================================")

total = correct + incorrect
percent = correct / total * 100
print("共计测试数量：" + str(total) + " 正确数量：" + str(correct) + " 错误数量：" + str(incorrect) + " 正确率:" + str(percent) + "%")


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
