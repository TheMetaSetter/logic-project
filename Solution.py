from CNFComponents import CNFSentence
from FileReader import CNFFileReader
from Solver import PL_Resolution

sentence = CNFFileReader("input5.txt")
CNFs = sentence.readSentence()

PL_Resolution(CNFs)

