#!/usr/bin/python

class TempTracker:
  def __init__(self):
    # for mode calculation
    # populate occurrences list with 0s from 0 to 140
    # since there's never been a recorded temp of > 140 ever
    self.occurrences = [0] * 140
    self.max_occurrences = 0
    self.mode = None

    # for mean
    self.n_readings = 0
    self.total_sum = 0
    self.mean = 0

    # for min and max
    self.min_temp = None
    self.max_temp = None

  def insert(self, temp):
    # for mode
    # increment number of times this temp has occurred
    self.occurrences[temp] += 1
    # update max_occurrences if necessary
    if self.occurrences[temp] > self.max_occurrences:
      self.mode = temp
      self.max_occurrences = self.occurrences[temp]
    # for mean
    self.n_readings += 1
    self.total_sum += temp
    self.mean = float(self.total_sum) / self.n_readings

    # for min and max
    if not self.max_temp or temp > self.max_temp:
      self.max_temp = temp
    
    if not self.min_temp or temp < self.min_temp:
      self.min_temp = temp
  
  def get_max(self):
    return self.max_temp

  def get_min(self):
    return self.min_temp

  def get_mean(self):
    return self.mean

  def get_mode(self):
    return self.mode


if __name__ == '__main__':
  tracker = TempTracker()
  tracker.insert(32)

  print(f"mean: {tracker.get_mean()}")  # should print 32.0
  print(f"min: {tracker.get_min()}")    # should print 32
  print(f"max: {tracker.get_max()}")    # should print 32
  print(f"mode: {tracker.get_mode()}")  # should print 32

  tracker.insert(135)

  print(f"mean: {tracker.get_mean()}")  # should print 83.5
  print(f"min: {tracker.get_min()}")    # should print 32
  print(f"max: {tracker.get_max()}")    # should print 135
  print(f"mode: {tracker.get_mode()}")  # can print either 32 or 135

  tracker.insert(135)

  print(f"mean: {tracker.get_mean()}")  # should print 100.66666666666667
  print(f"min: {tracker.get_min()}")    # should print 32
  print(f"max: {tracker.get_max()}")    # should print 135
  print(f"mode: {tracker.get_mode()}")  # should print 135