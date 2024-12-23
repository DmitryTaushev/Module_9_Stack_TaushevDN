import unittest

from task_1 import Stack

class TestStack(unittest.TestCase):
    stack = Stack(2)

    def test_1_init(self):
        self.assertEqual(self.stack.stack_size,2)
        self.assertEqual(self.stack.top,None)

    def test_2_push(self):
        self.stack.push('bottom_data')
        self.stack.push('top_data')
        self.assertEqual(self.stack.top.data, "top_data")
        self.assertEqual(self.stack.top.next_node.data, "bottom_data")
        self.assertEqual(self.stack.push('overflow_data'), "Стэк переполнен")

    def test_3_pop(self):
        self.stack.push('top_data')
        self.assertEqual(self.stack.pop(),'top_data')
        self.assertEqual(self.stack.top.data, 'bottom_data')

    def test_4_is_empty(self):
        self.assertEqual(self.stack.top.data,'bottom_data')
        self.stack.pop()
        self.assertEqual(self.stack.top,None)

    def test_5_if_full(self):
        self.stack.push('bottom_data')
        self.stack.push('top_data')
        self.assertEqual(self.stack.stack_size,2)

    def test_6_clear_stack(self):
        self.assertTrue(self.stack.top , True)

    def test_7_get_data(self):
        self.assertEqual(self.stack.get_data(0),'top_data')

    def test_8_size_stack(self):
        self.assertEqual(self.stack.size_stack(),2)

    def test_9_counter_int(self):
        self.assertEqual(self.stack.counter_int(),0)
        self.stack.pop()
        self.stack.pop()
        self.stack.push(3)
        self.assertEqual(self.stack.counter_int(),1)
