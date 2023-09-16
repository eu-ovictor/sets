from hypothesis import assume, given
from hypothesis.strategies import integers, sets
from typing import Set


IntSet = Set[int]

int_sets = sets(integers(), min_size=0)


@given(int_sets, int_sets)
def test_union(a: IntSet, b: IntSet):
    intersection = {x for x in a if x in b}

    union = a.union(b)

    assert len(union) == (len(a) + len(b)) - len(intersection)


@given(int_sets, int_sets)
def test_intersection(a: IntSet, b: IntSet):
    intersection = {x for x in a if x in b}

    assert len(intersection) == (len(a) + len(b)) - len(a.union(b))


@given(int_sets, int_sets)
def test_difference(a: IntSet, b: IntSet):
    differences = [(a - b, a, b), (b - a, b, a)]

    for difference, subtractor, subtractee in differences:
        intersection = {x for x in subtractor if x in subtractee}

        assert len(difference) == len(subtractor) - len(intersection)


@given(int_sets, int_sets)
def test_complement(a: IntSet, b: IntSet):
    assume(a.issubset(b))

    complement = b - a

    assert len(complement) == len(b) - len(a)
