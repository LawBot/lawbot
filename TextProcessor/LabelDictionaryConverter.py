from TextProcessor.LabeledCaseProcessor import LabeledCaseProcessor

in_path = '..\\input\\6818_tagged.txt'
yml_path = '..\\output\\out_6818.yml'
test_path = '..\\output\\test_6818.txt'

train_ratio = 0.9
lcp = LabeledCaseProcessor('INFO')
lcp.process(in_path, yml_path, test_path, train_ratio)