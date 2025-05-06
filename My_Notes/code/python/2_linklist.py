# 定义链表节点类
class Node:
    def __init__(self, data, next=None):
        self.data = data    # 节点存储的数据
        self.next = next    # 指向下一个节点的指针，默认为None


# 定义链表类
class LinkedList:
    def __init__(self):
        self.head = None    # 链表头节点，初始为空

    # 按值查找节点
    def find_by_value(self, value: int):
        p = self.head      # 从头节点开始
        while p and p.data != value:  # 遍历链表直到找到值或到达末尾
            p = p.next
        return p           # 返回找到的节点或None

    # 按索引查找节点
    def find_by_index(self, index: int):
        p = self.head      # 从头节点开始
        position = 0        # 当前位置计数器
        while p and position != index:  # 遍历直到找到索引位置或到达末尾
            p = p.next
            position += 1
        return p           # 返回找到的节点或None

    # 在指定索引前插入新节点
    def insert_before(self, index: int, value: int):
        new_node = Node(value)  # 创建新节点
        
        # 如果插入位置是0(链表头部)
        if index == 0:
            new_node.next = self.head  # 新节点指向原头节点
            self.head = new_node        # 更新头节点为新节点
        else:
            current = self.head
            position = 0
            # 找到要插入位置的前一个节点
            while current and position < index - 1:
                current = current.next
                position += 1
            
            # 如果索引超出范围
            if not current:
                raise IndexError("Index out of range")
            
            # 插入新节点
            new_node.next = current.next
            current.next = new_node

    # 按索引删除节点
    def delete_by_index(self, index: int):
        if not self.head:  # 空链表检查
            raise IndexError("Index out of range (empty list)")
        
        # 如果删除头节点
        if index == 0:
            self.head = self.head.next
        else:
            current = self.head
            position = 0
            # 找到要删除节点的前一个节点
            while current and position < index - 1:
                current = current.next
                position += 1
            
            # 如果索引无效
            if not current or not current.next:
                raise IndexError("Index out of range")
            
            # 跳过要删除的节点
            current.next = current.next.next

    # 按值删除节点
    def delete_by_value(self, value: int):
        if not self.head or not value:  # 空链表或空值检查
            return
        
        # 如果头节点就是要删除的节点
        if self.head.data == value:
            self.head = self.head.next
            return
        
        pre = self.head
        node = self.head.next
        not_found = False
        
        # 查找要删除的节点
        while node.data != value:
            if node.next:
                not_found = True
                break
            else:
                pre = node
                node = node.next
        
        # 如果找到则删除
        if not not_found:
            pre.next = node.next

    # 打印整个链表
    def print_all(self):
        if not self.head:  # 空链表检查
            print("Empty list")
            return
        
        current = self.head
        print(f"{current.data}", end="")  # 打印头节点
        current = current.next
        
        # 打印后续节点
        while current:
            print(f"->{current.data}", end="")
            current = current.next
        print()


if __name__ == '__main__':
    # 测试代码
    llist = LinkedList()
    llist.insert_before(0, 1)  # 链表: 1
    llist.insert_before(0, 2)  # 链表: 2->1
    llist.insert_before(1, 3)  # 链表: 2->3->1
    llist.insert_before(3, 4)  # 链表: 2->3->1->4
    llist.delete_by_index(0)   # 删除 2，链表变为 3->1->4
    llist.delete_by_value(3)   # 删除 3，链表变为 1->4
    llist.print_all()          # 输出: 1->4