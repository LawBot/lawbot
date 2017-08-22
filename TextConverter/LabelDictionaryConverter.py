from TextConverter.LabeledCaseProcessor import LabeledCaseProcessor

in_path = 'F:\Personal\OneDrive\小法博科技\产品\小法博\Documents\已完成标注（6818）.txt'
yml_path = 'output\\out_6818.yml'
test_path = 'output\\test_6818.txt'

lcp = LabeledCaseProcessor('INFO')
lcp.process(in_path, yml_path, test_path)