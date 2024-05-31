class SardinasPatterson:
    language = list()
    step = list()
    epsilon = ""    

    def divide(self, L1, L2):
        res = set()
        for elt in L1:
            for item in L2:
                if item.startswith(elt):
                    if(item[len(elt):] == ''):
                        self.epsilon = elt
                    res.add(item[len(elt):])
        return res
    
    def get_L1(self):
        res = self.divide(self.language, self.language)
        res.remove('')
        return res
    
    def get_L_n_plus_1(self, Ln):
        res = self.divide(Ln, self.language)
        return res.union(self.divide(self.language, Ln))
    
    def get_mot(self, lst, mot):
        for item in self.language:
            for elt in lst:
                if(item == (elt + mot)):
                    print("elt :", elt, " item", item, " mot : ", elt+mot)
                    return elt

        return mot

    def get_contre_exemple(self):
        res = []
        mot = self.epsilon
        temp = self.step
        res.append(mot)
        for i in range(len(temp) - 2, -1, -1 ):
            mot = self.get_mot(temp[i-1], mot)
            res.append(mot)
        return ''.join(res)

    def make_code(self):
        initial = self.language.copy()
        temp = initial.copy()
        temp_2 = None
        for i in range(len(temp)):
            self.language = initial.copy()
            temp = initial.copy()
            temp.pop(i)
            self.language = temp
            temp_2 = temp.copy()
            if(self.is_code()[0] == True):
                return self.language
            for j in range(len(temp_2)):
                temp_2.pop(j)
                self.language = temp_2
                if(self.is_code()[0] == True):
                    return self.language
        return list()

    def is_code(self):
        self.step.clear()
        if(len(self.language) == 1):
            return True, 'It stops at L1'
        temp = self.get_L1()
        count = 1
        self.step.append(temp)
        while('' not in temp):
            temp = self.get_L_n_plus_1(temp)
            if temp in self.step:
                return True, 'It stops at L' + str(count) 
            self.step.append(temp)
            count += 1
        self.step.append(self.language)
        return False, 'It stops at L' + str(count)
    