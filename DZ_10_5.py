import multiprocessing


class WarehouseManager():

    def __init__(self):
        self.data = multiprocessing.Manager().dict()

    def process_request(self, request):
        key, action, total = request
        if action == "receipt":
            if key in self.data:
                self.data[key] += total
            else:
                self.data[key] = total
        elif action == "shipment":
            if key in self.data and self.data[key] >= total:
                self.data[key] -= total

    def run(self, requests):
        processes = []
        for request in requests:
            p = multiprocessing.Process(target=self.process_request, args=(request,))
            processes.append(p)
            p.start()

        for p in processes:
            p.join()


if __name__ == '__main__':
    manager = WarehouseManager()
    requests = [
        ("product1", "receipt", 100),
        ("product2", "receipt", 150),
        ("product1", "shipment", 30),
        ("product3", "receipt", 200),
        ("product2", "shipment", 50)
    ]

    manager.run(requests)
    print(manager.data)
