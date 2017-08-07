# -*- coding: utf-8 -*-
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import logging

# Uncomment the following lines to enable verbose logging
# import logging
# logging.basicConfig(level=logging.INFO)

# logging.basicConfig(level=logging.DEBUG)

# Create a new instance of a ChatBot
bot = ChatBot(
    "Terminal",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    database_uri = "sqlite:///testdatabase.db",
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch'
        },
        {
            'import_path': 'chatterbot.logic.LowConfidenceAdapter',
            'threshold': 0.25,
            'default_response': 'What?'
        },

        # "chatterbot.logic.MathematicalEvaluation",
        # "chatterbot.logic.TimeLogicAdapter",
        # "chatterbot.logic.BestMatch"
    ],
    # trainer='chatterbot.trainers.ListTrainer',
    # trainer = ChatterBotCorpusTrainer,
    input_adapter="chatterbot.input.VariableInputTypeAdapter",
    output_adapter="chatterbot.output.OutputAdapter",
    # database="../database.db"
)

bot.set_trainer(ChatterBotCorpusTrainer)
# bot.train([
#     'How can I help you?',
#     'I want to create a chat bot',
#     'Have you read the documentation?',
#     'No, I have not',
#     'This should help get you started: http://chatterbot.rtfd.org/en/latest/quickstart.html',
#     'What is math?',
#     'Math is Science!',
#     'What does math do?',
#     'It calculates',
#     'software',
#     'A computer program which is written with programming code to realize certain functions',
#     '国际法',
#     '国际法（法语：Le droit international；英语：International Law，原称万国法[1]）又称国际公法，是主权国家国与国之间的法律。国际法不同于国家的法律制度，因为它主要的适用对象为国家而非公民，是规范政府组织之间关系的规则，有时也包括民族意识的法人和自然人等。国际法较无法约束各个国家，因为无法保障其法律体系始终顺利运作，因此缺乏有效制裁违法国家的制度。'
# ])

#bot.train("chatterbot.corpus.chinese.IntellectualPropertyLaw")
#bot.train("chatterbot.corpus.chinese.casestudy")
#bot.train(".corpus.IntellectualPropertyLaw")
#bot.train(".corpus.casestudy")
bot.read_only=True

input = {'2007年9月25日，被告向原告借款30000元':1, '现要求被告立即归还借款30000元':0}
output = bot.get_response(input)
print(output)

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
