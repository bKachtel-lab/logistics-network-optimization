from dataclasses import dataclass
from typing import List, Dict, Tuple
from client import Client
from entrepot import Entrepot

@dataclass
class Data:
    clients: List[Client]
    entrepots: List[Entrepot]
    couts: Dict[Tuple[str, str], float]  # (entrepot_id, client_id)

    def get_cost(self, i: str, j: str) -> float:
        return self.couts[(i, j)]