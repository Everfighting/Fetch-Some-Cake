# Python实现求一个集合所有子集的示例

# 方法一：回归实现


def PowerSetsRecursive(items):
    """Use recursive call to return all subsets of items, include empty set"""

    if len(items) == 0:
        # if the lsit is empty, return the empty list
        return [[]]

    subsets = []
    first_elt = items[0]  # first element
    rest_list = items[1:]

    # Strategy:Get all subsets of rest_list; for each of those subsets, a full subset list
    # will contain both the original subset as well as a version of the sebset that contains the first_elt

    for partial_sebset in PowerSetsRecursive(rest_list):
        subsets.append(partial_sebset)
        next_subset = partial_sebset[:] + [first_elt]
        subsets.append(next_subset)
    return subsets


def PowerSetsRecursive2(items):
    # the power set of the empty set has one element, the empty set
    result = [[]]
    for x in items:
        result.extend([subset + [x] for subset in result])
    return result


#方法二：二进制法
def PowerSetsBinary(items):
  #generate all combination of N items
  N = len(items)
  #enumerate the 2**N possible combinations
  for i in range(2**N):
    combo = []
    for j in range(N):
      #test jth bit of integer i
      if(i >> j ) % 2 == 1:
        combo.append(items[j])
    yield combo