
class LawCase:
    def __init__(self, case_id, case_content):
        self.id = case_id
        self.content = case_content

    def __init__(self, case_id):
        self.id = case_id

    def set_content(self, case_content):
        self.content = case_content