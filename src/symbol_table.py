from dataclasses import dataclass
from typing import Optional, Set, Any, List, Dict


@dataclass
class Symbol:
    name: str
    type_: str
    columns: Optional[Set[str]] = None  
    source: Optional[str] = None        
    value: Any = None                   

    def is_dataset(self) -> bool:
        return self.type_ == "dataset"

    def is_scalar(self) -> bool:
        return self.type_ == "scalar"

    def __getitem__(self, item):
        if item == "type":
            return self.type_
        return getattr(self, item)

    def get(self, item, default=None):
        try:
            return self[item]
        except (KeyError, AttributeError):
            return default

    def __str__(self) -> str:
        d = {"type": self.type_}
        if self.source:
            d["source"] = self.source
        if self.columns is not None:
            d["columns"] = self.columns
        if self.value is not None:
            d["value"] = self.value
        return str(d)

    def __repr__(self) -> str:
        return self.__str__()


class SymbolTable:
    def __init__(self):
        self.symbols: Dict[str, Symbol] = {}

    def declare(
        self,
        name: str,
        type_: str,
        columns: Optional[Set[str]] = None,
        source: Optional[str] = None,
        value: Any = None
    ) -> Symbol:
        symbol = Symbol(
            name=name,
            type_=type_,
            columns=columns,
            source=source,
            value=value
        )
        self.symbols[name] = symbol
        return symbol

    def lookup(self, name: str) -> Symbol:
        if name not in self.symbols:
            raise ValueError(f"Variable o dataset '{name}' no declarada previamente")
        return self.symbols[name]

    def exists(self, name: str) -> bool:
        return name in self.symbols

    def assign(self, name: str, value: Any):
        symbol = self.lookup(name)
        symbol.value = value

    def show(self) -> List[tuple]:
        return [
            (
                s.name,
                s.type_,
                sorted(list(s.columns)) if s.columns is not None else s.value
            )
            for s in self.symbols.values()
        ]

    def __repr__(self) -> str:
        return f"SymbolTable({list(self.symbols.keys())})"
