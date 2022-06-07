from pbs.pn_01018 import Q01018
from utils import duration_decorator


loop = 1


@duration_decorator(loop=loop)
def run():
    module = Q01018()
    module.solution()


if __name__ == '__main__':
    run()
