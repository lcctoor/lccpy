import re


class rindex:
    def __init__(self, index:int):
        assert type(index) is int
        assert index != 0
        self.index = index if (index <= -1) else index - 1
    
    @classmethod
    def parseIndex(cls, obj):
        if type(obj) is cls:
            return obj.index
        return obj


def _EditReturn(mode, value):
    if callable(value):
        def client(*vs, **kvs):
            vs = [rindex.parseIndex(x) for x in vs]
            kvs = {k:rindex.parseIndex(v) for k,v in kvs.items()}
            return _EditReturn(mode, value(*vs, **kvs))
        return client
    if mode == 1:
        return value + 1
    return value


class rslice:
    def __init__(self, core: list|tuple|str|bytes): self.core = core
    def __len__(self): return len(self.core)

    def __getattr__(self, name):
        mode = 0
        if r:= re.findall('_+$', name):
            l = re.findall('^_+', name) or ['']
            mode = len(r[0]) - len(l[0])
            if mode:
                name = name[:-mode]
        return _EditReturn(mode, self.core.__getattribute__(name))
    
    def __getitem__(self, key):
        key = self.getitemSlice(key)
        if [type(self.core), type(key)] == [bytes, int]:
            return bytes([self.core[key]])
        return self.core[key]

    def __setitem__(self, key, value):
        key = self.setitemSlice(key)
        try:
            self.core[key] = value  # list
        except:  # tuple, str, bytes
            if type(key) is int:
                if type(self.core) is tuple: value = (value, )
                if key == -1:
                    self.core = self.core[:key] + value
                else:
                    self.core = self.core[:key] + value + self.core[key+1:]
            else:
                a = key.start
                b = key.stop
                atype = type(a)
                btype = type(b)
                if atype is btype is int:
                    self.core = self.core[:a] + value + self.core[b:]
                elif atype is int:
                    self.core = self.core[:a] + value
                elif btype is int:
                    self.core = value + self.core[b:]
                else:
                    self.core = value
    
    def setitemSlice(self, key):
        if type(key) is int:
            if key <= -1: return key  # Python索引
            if key >= 1: return key - 1  # Python索引
        elif type(key) is slice:
            a = key.start
            b = key.stop
            atype = type(a)
            btype = type(b)
            if not {atype, btype} - {int, type(None)}:
                if atype is btype is int:
                    if a < 0 or b < 0:
                        size = len(self)
                        if a < 0: a = size + 1 + a  # R索引
                        if b < 0: b = size + 1 + b  # R索引
                    if a > b: a, b = b, a
                    if b < 1:
                        return slice(None, 0)  # 左侧插入
                    elif a >= 1:
                        return slice(a-1, b, None)
                    else:
                        return slice(None, b, None)
                
                elif atype is int:
                    if a >= 1: return slice(a-1, None)
                    return slice(a, None)
                
                elif btype is int:
                    if b >= 0: return slice(None, b)
                    if b == -1: return slice(None, None)
                    return slice(None, b + 1)
                
                else:
                    return slice(None, None)
        KeyError(key)

    def getitemSlice(self, key):
        if type(key) is int:
            if key <= -1: return key  # Python索引
            if key >= 1: return key - 1  # Python索引
        
        elif type(key) is slice:
            a = key.start
            b = key.stop
            c = key.step or 1
            atype = type(a)
            btype = type(b)
            ctype = type(c)
            if not {atype, btype, ctype} - {int, type(None)}:
                if c >= 1:
                    if atype is btype is int:
                        if a < 0 or b < 0:
                            size = len(self)
                            if a < 0: a = size + 1 + a  # R索引
                            if b < 0: b = size + 1 + b  # R索引
                        if max(a, b) >= 1:
                            if b >= a:
                                return slice(max(0, a-1), b, c)
                            else:
                                if b >= 2:
                                    return slice(a-1, b-2, -c)
                                return slice(a-1, None, -c)
                        else:
                            return slice(0, 0, c)
                    
                    elif atype is int:
                        if a >= 1: return slice(a-1, None, c)
                        return slice(a, None, c)
                    
                    elif btype is int:
                        if b >= 1: return slice(None, b, c)
                        if b == 0: return slice(0, 0, c)
                        if b == -1: return slice(None, None, c)
                        return slice(None, b + 1)
                    else:
                        return slice(None, None, c)
        raise KeyError(key)