import logging
import re

from TextProcessor.LawCase import LawCase

logger = logging.getLogger("raw_case_processor_logger")


class RawCaseProcessor:
    def __init__(self):
        self.logger = logging.getLogger("raw_case_processor_logger")
        self.logger.info('creating an instance of raw case processor')
    
    def readfile2lawcase(self, input_file):
        with open(input_file, encoding='utf-8') as f:
            content = f.readlines()
        
        case_str_list = []
        case_str = ''
        
        for idx, line in enumerate(content):
            if (line.startswith('【--') and not case_str == '') \
                or idx == len(content) - 1:
                case_str_list.append(case_str)
                case_str = ''
            case_str += line
        
        # print(case_str_list[-1])
        
        for case_str in case_str_list:
            lawcase = self.buildLawCase(case_str)
            if lawcase:
                print(lawcase.id)
                for accuse in lawcase.accuse_list:
                    print(accuse)
    
    def buildLawCase(self, case_str):
        content_str = str(case_str)
        lawcase_id = 0
        if content_str.find('【--') != -1 and content_str.find('--】') != -1:
            start_idx = str(case_str).find('【--') + len('【--')
            end_idx = str(case_str).index('--】')
            lawcase_id = str(case_str)[start_idx:end_idx]
        else:
            return None
        
        self.logger.debug("Building LawCase Object for case: " + lawcase_id)
        
        if content_str.find('[原告诉称]') == -1:
            logger.debug("This case does not have [原告诉称] field: " + lawcase_id)
            return None
        
        lawcase = LawCase(lawcase_id)
        start_idx = content_str.find('[原告诉称]') + len('[原告诉称]')
        end_idx = content_str.find('[', start_idx)
        accuse_str = content_str[start_idx:end_idx]
        
        index_list = []
        for index in range(len(accuse_str)):
            if accuse_str[index] == '，':
                index_list.append(index)
        
        # Remove , in big numbers
        for index in range(len(index_list) - 1, 0, -1):
            if accuse_str[index_list[index] - 1].isdigit() and accuse_str[index_list[index] + 1].isdigit():
                accuse_str = accuse_str[:index_list[index]] + accuse_str[index_list[index] + 1:]
        
        accuse_str = accuse_str.strip().replace('\n', '')
        
        accuse_list = re.split('，|。|；', accuse_str)
        
        if not accuse_list[-1]:
            accuse_list = accuse_list[:-2]
        
        lawcase.set_accuse_list(accuse_list)
        return lawcase
