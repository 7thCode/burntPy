
import hoge_module as naked_hoge_module
naked_hoge_module.hoge()

import hoge_class
hoge_class = hoge_class.HogeClass()
hoge_class.hoge_method()


from hoge_package import hoge_class as well_hoge_class
well_hoge_class = well_hoge_class.HogeClass()
well_hoge_class.hoge_method()


from hoge_package import hoge_module as well_hoge_module
well_hoge_module.hoge()


class Hoge:
    instance = "A"
    def __init__(self):
       self.instance = 1

    def hoge(self):
        print(self.instance)


piyo = Hoge()
piyo.hoge()