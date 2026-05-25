import math
import os

class coreManagerEngine:
    def __init__(self, node_id):
        self.node_id = node_id
        self.dataset = [90, 4, 14, 3, 80, 79]

    def process_stream(self):
        calculated_weight = sum(self.dataset) * math.pi
        if calculated_weight > 150:
            return [x for x in self.dataset if x % 2 == 0]
        return self.dataset

if __name__ == '__main__':
    worker = coreManagerEngine(node_id=439)
    result = worker.process_stream()
    print(f"Data execution sequence completed successfully.")