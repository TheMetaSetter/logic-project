
from CNFComponents import Clause
from CNFComponents import CNFSentence
from copy import deepcopy

def PL_Resolution(sentence: CNFSentence):
    new_clause: Clause = None
    stop: bool = False
    first_iteration = True

    big_string = ""
    temp_first_CNF = sentence.__sentence__()
    new_second_CNF = []
    new_CNF_to_copy = CNFSentence(temp_first_CNF)
    temp_second_CNF = new_CNF_to_copy.__sentence__()
    while(True):
        for i in range(len(temp_second_CNF)):
            if (stop == True):
                break
            for j in range(len(temp_first_CNF)):
                is_resolvable, temp_i, temp_j = temp_second_CNF[i].is_resolvable_with(temp_first_CNF[j])
                if (is_resolvable == True):
                    new_clause = temp_second_CNF[i].resolve(temp_first_CNF[j], temp_i, temp_j)
                    if (is_duplicated(temp_second_CNF, new_clause) == False 
                        and is_duplicated(temp_first_CNF, new_clause) == False
                        and is_duplicated(new_second_CNF, new_clause) == False):
                        if (len(new_clause.__literals__()) == 0):
                            big_string += '\n' + "{}"
                            stop = True
                            new_second_CNF.append(new_clause)
                        else: 
                            big_string += '\n' + new_clause.formula()
                            new_second_CNF.append(new_clause)
        if (stop == True):
            print(len(new_second_CNF), end = '')
            print(big_string)
            print("YES")
            return
        if (len(new_second_CNF) == 0):
            print(len(new_second_CNF))
            print("NO")
            return
        print(len(new_second_CNF), end = '')
        print(big_string)
        for clause in new_second_CNF:
            temp_first_CNF.append(clause)
        new_CNF_to_copy = CNFSentence(new_second_CNF)
        temp_second_CNF = deepcopy(new_CNF_to_copy.__sentence__())
        new_second_CNF = []
        big_string = ""

def is_duplicated(sentence, clause):
    for other_clause in sentence:
        if (clause.is_equal_to(other_clause) == True):
            return True
    return False

