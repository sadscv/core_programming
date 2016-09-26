def test():
    ns = {}
    code = 'x = 1'
    exec(code, ns)
    print(ns)
test()