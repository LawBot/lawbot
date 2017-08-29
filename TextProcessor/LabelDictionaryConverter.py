from TextProcessor.LabeledCaseProcessor import LabeledCaseProcessor

in_path = '..\\input\\2003_tagged.txt'
yml_path = '..\\output\\out_2003.yml'
test_path = '..\\output\\test_2003.txt'

train_ratio = 0.9
lcp = LabeledCaseProcessor('DEBUG')
lcp.process(in_path, yml_path, test_path, train_ratio)