# -*- coding: utf-8 -*-
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Uncomment the following lines to enable verbose logging
import logging
# logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.DEBUG)

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

input = '口头约定月利率为0.8%'
output = bot.get_response(input)
print(output)
