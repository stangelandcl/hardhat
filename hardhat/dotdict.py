from pprint import pformat


class dotdict(dict):
    """Access attributes like a class: X.attr instead of X['attr']"""
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__

    def __getattr__(self, attr):
        if not attr in self:
            raise Exception('Missing attribute %s' % attr)
        
        return self.get(attr)

    def __str__(self):
        return pformat(self, indent=4)
