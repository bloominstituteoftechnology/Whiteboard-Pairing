"""
Since we have a highest possible score, we can use 
a strategy known as a counting sort into to achieve
a runtime faster than O(n log n).
"""
def sort_top_scores(scores, highest_possible_score):
  # init a list with length highest_possible_score filled with 0s
  score_counts = [0] * highest_possible_score
  # increment the value at the index of each score so 
  # we get the count of how many times each score appears
  for score in scores:
    score_counts[score] += 1
  # list to hold the sorted scores
  sorted_scores = []
  # iterate through our score_counts list
  # for each count, append the score that many number 
  # of times to our sorted_scores list
  for score in range(highest_possible_score, -1, -1):
    count = score_counts[score]
    # even though there is a nested loop in this for loop,
    # think about what the time complexity of this function
    # is in terms of the total number of input elements
    for i in range(count):
      sorted_scores.append(score)

  return sorted_scores