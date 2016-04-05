# class ConsCell():
#     def __init__(self, left = None, right = None):
#         self.left = left
#         self.right = right

#     def __str__(self):
#         return (str(self.left) + " : " + str(self.right))

class ConsCell():
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return (str(self.value) + " => " +str(self.left) + " : " + str(self.right))