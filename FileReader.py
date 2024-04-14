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
            j = 0
            while (j < len(extra_line)):
                if (extra_line[j] == ' '):
                        j += 1
                        continue
                if (extra_line[j] == '-'):
                    extra_clause = Clause([Literal(ord(extra_line[j + 1]), False)])
                    j += 6
                else:
                    extra_clause = Clause([Literal(ord(extra_line[j]), True)])
                    j += 5
                newCNFSentence.append(extra_clause)

            # Read the number of clauses in the sentence
            num_of_clauses = (int)(f.readline())

            # Read the clauses
            for i in range(0, num_of_clauses):
                newClause = []
                line = f.readline()
                j = 0
                while (j < len(line)):
                    if (line[j] == ' '):
                        j += 1
                        continue
                    if (line[j] == '-'):
                        newLiteral = Literal(ord(line[j + 1]), True)
                        j += 6
                    else:
                        newLiteral = Literal(ord(line[j]), False)
                        j += 5
                    newClause.append(newLiteral)
                tempClause = Clause(newClause)
                tempClause.reorder()
                newCNFSentence.append(tempClause)
            return CNFSentence(newCNFSentence)
    