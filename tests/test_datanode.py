import unittest
from core.data_node import *

class TestDataNode(unittest.TestCase):
    def setUp(self) -> None:
        self.object = "Abhinav"
        self.metadata = {"city" : "Junnar"}
        self.node = DataNode(self.object, self.metadata)
        return super().setUp()
    
    def test_object_property(self):
        self.assertEqual(self.node.object, self.object)

    def test_metadata_property(self):
        self.assertEqual(self.node.metadata, self.metadata)


if __name__ == '__main__':
    unittest.main()