from TextProcessor.LabeledCaseProcessor import LabeledCaseProcessor

in_path = '..\\input\\2003_tagged_mod.txt'
yml_path = '..\\output\\out_2003_mod.yml'
test_path = '..\\output\\test_2003_mod.txt'

train_ratio = 0.9
lcp = LabeledCaseProcessor('DEBUG')
lcp.process(in_path, yml_path, test_path, train_ratio)