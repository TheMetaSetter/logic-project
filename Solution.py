from CNFComponents import CNFSentence
from FileReader import CNFFileReader
from Solver import PL_Resolution

sentence = CNFFileReader.readSentence("input.txt")

PL_Resolution(sentence)

