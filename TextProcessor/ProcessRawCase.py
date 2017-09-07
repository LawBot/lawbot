import logging
from TextProcessor.RawCaseProcessor import RawCaseProcessor

if __name__ == "__main__":
	logger = logging.getLogger("raw_case_processor_logger")
	logger.setLevel(logging.INFO)

	ch = logging.StreamHandler()
	ch.setLevel(logging.INFO)

	logger.addHandler(ch)

	rcp = RawCaseProcessor()
	rcp.readfile2lawcase("..\\input\\2007.txt")