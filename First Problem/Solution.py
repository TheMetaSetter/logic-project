from FileReader import CNFFileReader
from Solver import PL_Resolution

sentence = CNFFileReader("First Problem/input.txt")
CNFs = sentence.readSentence()

PL_Resolution(CNFs)

