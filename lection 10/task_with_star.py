# Есть маркер @pytest.mark.id_check(1, 2, 3), нужно вывести на печать, то что в него передано
#
# >>> 1, 2, 3

import pytest


@pytest.mark.id_check(5, 6, 7)
def test(request):
    # Здесь пишем код
    # print('\n', request.node.get_closest_marker("id_check").args, sep='')
    mark_args = test.pytestmark[0].args
    print('\n', mark_args, sep='')
