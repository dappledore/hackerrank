# https://www.hackerrank.com/challenges/permutation-equation/problem

def permutationEquation(p):
    n = len(p)
    # create p(1) , p(2) .. list.    e.x. p(1) = p[0]
    return [p.index(p.index(i)+1)+1 for i in range(1, n+1)]

    # # call p(p(v)) to get index minus 1 , get value from p list
    # arr = [p[vals[vals[v]]-1] for v in p]
    # return arr


print(permutationEquation([2, 5, 11, 10, 1, 14,
                           7, 3, 16, 9, 8, 6, 18, 12, 15, 17, 13, 4]))
