def insert(self, val):
        if self.root is None:
            self.root=Node(val)
        else:
            current = self.root
            while True:
                if val < current.info:
                    if current.left is None:
                        current.left=Node(val)
                        break
                    else:
                        current=current.left
                else:
                    if current.right is None:
                        current.right=Node(val)
                        break
                    else:
                        current=current.right
