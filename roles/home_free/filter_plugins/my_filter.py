import re


def filter_it(inp):
    result = re.findall(r'Filesystem.*|.*/$', inp, flags=re.MULTILINE)
    return result


class FilterModule():
    '''filters smth'''

    def filters(self):
        return {
            'get_free_space': filter_it
        }
