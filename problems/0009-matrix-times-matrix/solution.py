def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:


    if len(a[0]) != len(b):
        return -1

    res: list[list[int|float]] = []

    for i in range(len(a)):
        curr_res: list[int|float] = []
        for j in range(len(b[0])):
            curr_res.append(dot_product(a[i], get_col(b, j)))

        res.append(curr_res)
        
    return res


def dot_product(a: list[int|float], b: list[int|float]):
    res = 0

    for i in range(len(a)):
        res += a[i] * b[i]

    return res



def get_col(a: list[list[int|float]], i):
    return [row[i] for row in a]