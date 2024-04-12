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
        newCNFSentence = list[Clause]
        with open(self.__filename, "r") as f:
            # Read the alpha
            extra_line: str = f.readline()
            if (extra_line[0] == '-'):
                extra_clause: Clause = {Literal(extra_line[1], True)}
            else:
                extra_clause: Clause = {Literal(extra_line[0], False)}
            newCNFSentence.append(extra_clause)

            # Read the number of clauses in the sentence
            num_of_clauses = f.read()

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
    