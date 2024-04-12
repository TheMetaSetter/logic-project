from CNFComponents import Literal
from CNFComponents import Clause
from CNFComponents import CNFSentence

class CNFFileReader:
    """
    A class to read a CNF sentence from a file.
    
    Attributes:
    - filename: Name of the file to read the map from.
    
    Methods:
    - readSentence(): Reads the sentence from the file and returns a CNFSentence object.
    
    Example:
    >>> reader = CNFFileReader("cnf.txt")
    >>> map2d = reader.readSentence()
    """

    __filename: str
    
    def __init__(self, filename: str):
        self.__filename = filename

    def readSentence(self) -> CNFSentence:
        newCNFSentence = []
        with open(self.__filename, "r") as f:
            # Read the alpha
            extra_line: [] = f.readline()
            if (extra_line[0] == '-'):
                extra_clause = Clause([Literal(ord(extra_line[1]), False)])
            else:
                extra_clause = Clause([Literal(ord(extra_line[0]), False)])
            newCNFSentence.append(extra_clause)

            # Read the number of clauses in the sentence
            num_of_clauses = (int)(f.readline())

            # Read the clauses
            for i in range(0, num_of_clauses):
                newClause = []
                line = f.readline()
                for j in range(0, len(line)):
                    if (line[j] != 'O' and line[j] != '-' and line[j] != '\n'
                        and line[j] != ' ' and line[j] != 'R'):
                        if (line[j - 1] == '-'):
                            newLiteral = Literal(ord(line[j]), False)
                        else:
                            newLiteral = Literal(ord(line[j]), True)
                        newClause.append(newLiteral)
                newCNFSentence.append(Clause(newClause))
            return CNFSentence(newCNFSentence)
    