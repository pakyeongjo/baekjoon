from pbs.pn_02751 import Q02751
from utils import duration_decorator


loop = 1


@duration_decorator(loop=loop)
def run():
    module = Q02751()
    module.solution()


if __name__ == '__main__':
    run()
