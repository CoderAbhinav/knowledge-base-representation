class DataNode:
    def __init__(self, object_: object, meta: dict = {}, relations: dict = {}) -> None:
        self.__object: object = object_
        self.__meta: dict = meta
        self.__id: str = hash(object)

    @property
    def object(self) -> object:
        return self.__object

    @property
    def metadata(self) -> dict:
        return self.__meta
    
    @property
    def id(self) -> str:
        return self.__id

    def __repr__(self) -> str:
        return ""
    

