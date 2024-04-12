
from CNFComponents import Clause
from CNFComponents import CNFSentence

def PL_Resolution(sentence: CNFSentence, clause: Clause):
    new_CNF = CNFSentence(sentence)
    new_clause: Clause = None
    stop: bool = False
    while(True):
        new_CNF_to_copy = CNFSentence()
        for i in range(len(new_CNF.__sentence)):
            for j in range(len(sentence.__sentence)):
                if (new_CNF.__sentence[i].is_resolvable_with(sentence.__sentence[j])):
                    new_clause = new_CNF.__sentence[i].resolve(sentence.__sentence[j])
                    if (len(new_clause.__literals) == 0):
                        stop = True
                    else: 
                        print(new_clause.formula())
                        print('\n')
                        new_CNF_to_copy.__sentence.append(new_clause)
        if (len(new_CNF_to_copy.__sentence) == 0):
            print("NO")
        if (stop == True):
            print("YES")


