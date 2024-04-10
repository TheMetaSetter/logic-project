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
        with open(self.__filename, "r") as f:
            # Read the number of clauses in the sentence
            num_of_clauses = f.read()
            
            newCNFSentence = list[Clause]

            # Read the clauses
            for i in range(0, num_of_clauses):
                newClause = list[Literal]
                line = f.readline()
                for j in range(0, len(line)):
                    if (line[j] != 'O' and line[j] != '-' 
                        and line[j] != ' ' and line[j + 1] != 'R'):
                        if (line[j - 1] == '-'):
                            newLiteral = Literal(j, False)
                        else:
                            newLiteral = Literal(j, True)
                        newClause.append(newLiteral)
                newCNFSentence.append(newClause)
            return CNFSentence(newCNFSentence)
    