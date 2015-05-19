## Clawer for HTML ##
import urllib2, re
KKre = re.compile('<h[0-9]+[^>]+>')
KKptag = re.compile('<p>(.*?)</p>')

class SimpleClawer:
    def __init__(self, startpage):
        self.startpage = startpage

    def ParseKK(self, cfile):
        tmpP = []
        tmpH = []

        f = open(cfile)
        n = 0
        for line in f:
            line = line.strip()
            n += 1
            if '<p>' in line:
                tmpP.append('%d\t%s' % (n, line))
                continue
            m = KKre.search(line)
            if m: tmpP.append(line)
        f.close()
        return tmpP
