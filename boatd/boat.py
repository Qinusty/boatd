class Boat(object):
    def __init__(self, driver):
        self.driver = driver

    def __getattr__(self, name):
        func = vars(self.driver.module).get(name)
        if func is None:
            raise AttributeError(
                    "'{}' driver has no attribute '{}'".format(
                        self.driver.path,
                        name)
            )
        else:
            return func