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
	database_uri="sqlite:///2003database.db",
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
bot.train("corpus.out_2003")
bot.read_only = True

print("Train Complete")
