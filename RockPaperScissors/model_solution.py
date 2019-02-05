#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  outcomes = []
  plays = ['rock', 'paper', 'scissors']

  def find_outcome(rounds_left, result=[]):
    if rounds_left == 0:
      outcomes.append(result)
      return
    for play in plays:
      find_outcome(rounds_left - 1, result + [play])

  find_outcome(n, [])
  return outcomes

if __name__ == "__main__":
  rv1 = rock_paper_scissors(2)
  print(rv1)  # should print [['rock', 'rock'], ['rock', 'paper'], ['rock', 'scissors'], ['paper', 'rock'], ['paper', 'paper'], ['paper', 'scissors'], ['scissors', 'rock'], ['scissors', 'paper'], ['scissors', 'scissors']]

  rv2 = rock_paper_scissors(3)
  print(len(rv2))  # should print 27

  rv3 = rock_paper_scissors(4)
  print(len(rv3))  # should print 81

  rv4 = rock_paper_scissors(5)
  print(len(rv4))  # should print 243