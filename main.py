from pbs.pn_11720 import Q11720
from utils import duration_decorator


loop = 1


@duration_decorator(loop=loop)
def run():
    module = Q11720()
    module.solution()


if __name__ == '__main__':
    run()
