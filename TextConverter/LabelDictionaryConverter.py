from TextConverter.LabeledCaseProcessor import LabeledCaseProcessor

in_path = 'F:\Personal\OneDrive\小法博科技\产品\小法博\Documents\【张旭】标注1608-3208.txt'
yml_path = 'output\\out.yml'
test_path = 'output\\test.txt'

lcp = LabeledCaseProcessor('INFO')
lcp.process(in_path, yml_path, test_path)