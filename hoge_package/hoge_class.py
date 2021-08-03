class HogeClass:
    instance_value = "instance from hoge_package."

    def hoge_method(self):
        print(self.instance_value)

if __name__ == "__main__":
    # test code
    HogeClass.hoge_method()