class BinaryTree:
    def __init__(self, root=None):
        self.root = root
        
    def pre_order(self):
        values = []

        def walk(root):
            if root is None:
                return
            values.append(root.value)
            walk(root.left)
            walk(root.right)
        
        walk(self.root)
        return values

    def in_order(self):
        values = []

        def walk(root):
            if root is None:
                return
            walk(root.left)
            values.append(root.value)
            walk(root.right)
        walk(self.root)
        return values

    def post_order(self):
        values = []

        def walk(root):
            if root is None:
                return
            walk(root.left)
            walk(root.right)
            values.append(root.value)
        walk(self.root)
        return values
    
    def get_max(self):
        if self.root is None:
            return None
        self.max = self.root.value
        
        def walk(root):
            if root is None:
                return
            if root.value > self.max:
                self.max = root.value
            walk(root.left)
            walk(root.right)
        walk(self.root)
        return self.max