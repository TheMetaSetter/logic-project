
from CNFComponents import Clause
from CNFComponents import CNFSentence

def PL_Resolution(sentence: CNFSentence):
    new_clause: Clause = None
    stop: bool = False
    
    temp_first_CNF = sentence.__sentence__()
    new_second_CNF = sentence.__sentence__()
    while(True):
        new_CNF_to_copy = CNFSentence(new_second_CNF)
        temp_second_CNF = new_CNF_to_copy.__sentence__()
        for i in range(new_CNF_to_copy.__len__()):
            for j in range(sentence.__len__()):
                is_resolvable, temp_i, temp_j = temp_second_CNF[i].is_resolvable_with(temp_first_CNF[j])
                if (is_resolvable == True):
                    new_clause = temp_second_CNF[i].resolve(temp_first_CNF[j], temp_i, temp_j)
                    if (len(new_clause.__literals__()) == 0):
                        stop = True
                    else: 
                        print(new_clause.formula())
                        print('\n')
                        new_second_CNF.append(new_clause)
        if (len(temp_second_CNF) == 0):
            print("NO")
            return
        if (stop == True):
            print("YES")
            return


