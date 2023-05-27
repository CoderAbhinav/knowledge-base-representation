from data_node import DataNode


class Relation:
    def __init__(self, to: DataNode,  weight: float = 0.0, relation: str = "") -> None:
        self.weight: float = weight
        self.to: DataNode = to
        self.relation: str = relation
    
    @property
    def to(self) -> DataNode:
        return self.to