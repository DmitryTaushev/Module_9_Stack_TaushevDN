"""Это класс узла"""
class Node:
    """Метод инициализации узла"""
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

"""Класс стэка"""
class Stack:
    """Метод инициализации стэка"""
    def __init__(self, stack_size=5, top=None):
        self.stack_size = stack_size
        self.top = top  # через топ обращаемся к атрибутам ноды
    """Метод добавления элемента в стэк и назначения вершины"""
    def push(self, data):
        if self.size_stack() < self.stack_size:
            new_node = Node(data)
            new_node.next_node = self.top  # та вершина которая была
            self.top = new_node  # переназначаем вершину
        else:
            print("Стэк переполнен")
            return "Стэк переполнен"
    """Метод удаления элемента и переназначения вершины"""
    def pop(self):
        if self.top:
            remove_last = self.top
            self.top = self.top.next_node
            return remove_last.data
        else:
            return "Стэк пуст"
    """Методы определения наличия элементов в стэке"""
    def is_empty(self):
        if self.top:
            return False
        else:
            return True

    def is_full(self):
        if self.stack_size == self.size_stack():
            return True
        else:
            return False
    """Метод очистки стэка от элементов"""
    def clear_stack(self):
        while self.top:
            self.pop()
    """Метод возвращающий стэк под определенным индексом"""
    def get_data(self, index):
        counter = 0
        stack_item = self.top
        while stack_item:
            if counter == index:
                return stack_item.data
            stack_item = stack_item.next_node
            counter += 1
        return f"Out of range"
    """Метод определения размера стэка"""
    def size_stack(self):
        counter = 0
        stack_item = self.top
        while stack_item:
            counter += 1
            stack_item = stack_item.next_node
        return counter
    """Метод показывающий количество стэков с целочисленными данными"""
    def counter_int(self):
        counter = 0
        stack_item = self.top
        while stack_item:
            if isinstance(stack_item.data, int):
                counter += 1
            stack_item = stack_item.next_node
        return counter

"""Определяем класс Stack как stack"""
stack = Stack()
"""Создаем стэки"""
stack.push(1)
stack.push("sta")
stack.push(2)
stack.push(2.5)
stack.push("sta")
"""Выводим на экран результат работы функции по подсчету стэков с целочисленными данными"""
print(stack.counter_int())
