class GrammarStats:
    def __init__(self):
        self.grammar_check_list = []
        pass

    def check(self, text):
        punctuation = "!.?"
        if text[0].isupper() and text[-1] in punctuation:
            result = True
            self.grammar_check_list.append(True)
            return True
        else:
            self.grammar_check_list.append(False)
            return False 
    

    def percentage_good(self):
        list_total = len(self.grammar_check_list)
        list_of_true = []
        if len(self.grammar_check_list) == 0:
            return 0
        for x in self.grammar_check_list:
            if x == True:
                list_of_true.append(x)     #how many checks are True
                
        decimal_percent = len(list_of_true) / list_total   #percentage = True / total = 0.50
        percentage = decimal_percent * 100   #new percentage = percentage * 100
        return percentage


        #   int: the percentage of texts checked so far that passed the check
        #        defined in the `check` method. The number 55 represents 55%.
    
