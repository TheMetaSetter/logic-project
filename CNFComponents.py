import string 

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
        self.__symbol = symbol
        self.__isNot = isNot
    
    def formula(self) -> string:
        return self.__symbol
        
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
        self.__literals = literals
    
    def formula(self) -> string:
        clauseString = ""
        for i in len(self.__literals):
            if (self.__literals[i].is_negative() == True):
                clauseString += '-'
            clauseString += self.__literals[i].formula()
            if (i != len(self.__literals) - 1):
                clauseString += " OR "
        return clauseString
        
    def is_resolvable_with(self, otherClause) -> tuple[bool, int, int]:
        for i in len(self.__literals):
            for j in len(otherClause.__literals):
                if (self.__literals[i].formula() == otherClause.__literals[j].formula() 
                    and self.__literals[i].is_negative() != otherClause.__literals[j].is_negative()):
                    return tuple[True, i, j]
        return tuple[False, 0, 0]
    
    def resolve(self, otherClause, pos_i, pos_j):
        newList = list[Literal] 
        self.__literals.pop(pos_i)
        otherClause.__literals.pop(pos_j)
        thisSize = len(self.__literals)
        otherSize = len(otherClause.__literals)
        i, j = 0, 0
        while (i < thisSize and j < otherSize):
            if (self.__literals[i].__symbol() < otherClause.__literals[j].__symbol()):
                newList.__add__(self.__literals[i])
                i += 1
                continue
            if (self.__literals[i].__symbol() > otherClause.__literals[j].__symbol()):
                newList.__add__(otherClause.__literals[j])
                j += 1
                continue
            if (self.__literals[i].is_negative() == otherClause.__literals[j].is_negative()):
                newList.__add__(otherClause.__literals[j])
            i += 1
            j += 1
        while (i < thisSize):
            newList.__add__(self.__literals[i])
            i += 1
        while (j < otherSize):
            newList.__add__(otherClause.__literals[j])
            j += 1
        return newList
    
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
        self.__sentence = sentence
    
    def formula(self) -> string:
        sentenceString = "("
        for i in len(self.__sentence):
            sentenceString += self.__sentence[i].formula()
            if (i != len(self.__sentence) - 1):
                sentenceString += ") AND ("
        sentenceString += ')'
        return sentenceString