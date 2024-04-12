from __future__ import annotations
class Literal:
    """A class representing a data structure that is a symbol of a logic sentence
    
    Attributes:
    - symbol: A character to represent itself in the logic sentence
    - isNot: Not or Not Not
    
    Methods:
    - formula(): To return its symbol
    - isNegative(): To return its Not status
    
    
    Example:
    >>> literal = Literal('A', False)
    >>> literalString = literal.formula()
    """

    def __init__(self, symbol: int, isNot: bool):
        self.__symbol: int = symbol
        self.__isNot: bool = isNot
        
    def __num__(self) -> int:
        return self.__symbol
    
    def formula(self) -> str:
        return str(self.__symbol)
        
    def is_negative(self) -> bool:
        return self.__isNot


class Clause:
    """A class representing a data structure that is a clause of a logic sentence
    
    Attributes:
    - literals: an array of Literal
    
    Methods:
    - formula(): To return its clause
    - is_resolvable_with(Clause): To check if it is resolvable with another clause
    - resolve(Clause): To resolve with another clause
    
    Example:
    >>> clause = Clause({Literal('A', True), Literal('B', False)})
    >>> string clauseString = clause.formula()
    """
    
    def __init__(self, literals: list[Literal]):
        self.__literals: list[Literal] = literals
    
    def formula(self) -> str:
        clauseString = ""
        literals = self.__literals__()
        for i in range(len(literals)):
            if (literals[i].is_negative() == True):
                clauseString += '-'
            clauseString += literals[i].formula()
            if (i != len(literals) - 1):
                clauseString += " OR "
        return clauseString
        
    def is_resolvable_with(self, otherClause: Clause) -> tuple[bool, int, int]:
        this_literals: list[Literal] = self.__literals__()
        other_literals: list[Literal] = otherClause.__literals__()
        for i in range(len(this_literals)):
            for j in range(len(other_literals)):
                if (this_literals[i].formula() == other_literals[j].formula()
                    and this_literals[i].is_negative() != other_literals[j].is_negative()):
                    return True, i, j
        return False, 0, 0
    
    def resolve(self, otherClause, pos_i, pos_j):
        this_literals: list[Literal] = self.__literals__()
        other_literals: list[Literal] = otherClause.__literals__()
        
        newList = []
        this_literals.pop(pos_i)
        other_literals.pop(pos_j)
        thisSize = len(self.__literals)
        otherSize = len(other_literals)
        i, j = 0, 0
        while (i < thisSize and j < otherSize):
            if (this_literals[i].__num__() < other_literals[j].__num__()):
                newList.append(this_literals[i])
                i += 1
                continue
            if (this_literals[i].__num__() > other_literals[j].__num__()):
                newList.append(other_literals[j])
                j += 1
                continue
            if (this_literals[i].is_negative() == other_literals[j].is_negative()):
                newList.append(other_literals[j])
            i += 1
            j += 1
        while (i < thisSize):
            newList.append(this_literals[i])
            i += 1
        while (j < otherSize):
            newList.append(other_literals[j])
            j += 1
        return Clause(newList)
    
    def __literals__(self) -> list[Literal]:
        return self.__literals
        
    
class CNFSentence:
    """A class representing a data structure that is a logic sentence
    
    Attributes:
    - __sentence: a logic sentence
    
    Methods:
    - formula(): To return its sentence
    
    Example:
    >>> sentence = CNFSentence({Clause, Clause})
    >>> string sentenceString = sentence.formula()
    """
    
    def __init__(self, sentence: list[Clause]):
        self.__sentence: list[Clause] = sentence
    
    def formula(self) -> str:
        sentenceString = "("
        for i in range(len(self.__sentence)):
            sentenceString += self.__sentence[i].formula()
            if (i != len(self.__sentence) - 1):
                sentenceString += ") AND ("
        sentenceString += ')'
        return sentenceString
    
    def __len__(self) -> int:
        return len(self.__sentence)
    
    def __sentence__(self) -> list[Clause]:
        return self.__sentence