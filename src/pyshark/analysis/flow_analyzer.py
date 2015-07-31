__author__ = 'milos'

# TODO: Tested with .PCAP files only, live capturing must be revised!!!


class FlowAnalyzer(object):

    def __init__(self, capture, attrs):
        """

        :param capture:
        :param attrs:
        :return:
        """

        self._capture = capture
        self.attrs = attrs


    def get_summary(self):

        def deep_getattr(o, attr):
            _o = o
            try:
                for a in attr.split('.'):
                    _o = getattr(_o, a)
                return _o
            except:
                return None

        data = []
        for p in self._capture:
            line = [deep_getattr(p, x) for x in self.attrs]
            data.append(line)

        return data