def begin_end(decorated):
    def outer_func(*params, **extend):

        print("-> decorater")
        print(params)
        print(extend)
        print("decorater ->")

        print(decorated(*params, **extend))

    return outer_func
