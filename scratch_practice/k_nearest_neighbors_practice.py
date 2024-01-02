from typing import List, NamedTuple
from collections import Counter

import linear_algebra_practice as la

Vector = List[float]

def raw_majority_vote(labels: List[str]) -> str:
    votes = Counter(labels)
    winner, _ = votes.most_common(1)[0]
    return winner

assert raw_majority_vote(['a', 'b', 'c', 'b']) == 'b'

def majority_vote(labels: List[str]) -> str:
    """Assumes that labels are ordered from nearest to farthest."""
    vote_counts = Counter(labels)
    winner, winner_count = vote_counts.most_common(1)[0]
    num_winners = len([count
                       for count in vote_counts.values()
                       if count == winner_count])
    
    if num_winners == 1:
        return winner
    else:
        return majority_vote(labels[:-1]) # try again without the farthest
    
assert majority_vote(['a', 'b', 'c', 'b', 'a']) == 'b'

class LabeledPoint(NamedTuple):
    point: Vector
    label: str

def knn_classify(k: int,
                 labeled_points: List[LabeledPoint],
                 new_point: Vector) -> str:
    
    # Order the labeled points from nearest to farthest
    by_distance = sorted(labeled_points, key=lambda lp: la.distance(lp.point, new_point))

    # Find the labels for the k closet
    k_nearest_labels = [lp.label for lp in by_distance[:k]]

    # and let them vote.
    return majority_vote(k_nearest_labels)