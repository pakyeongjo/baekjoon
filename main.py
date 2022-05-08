from pbs.pn_10610 import Q10610
from utils import duration_decorator


loop = 1


@duration_decorator(loop=loop)
def run():
    module = Q10610()
    module.solution()


if __name__ == '__main__':
    run()
