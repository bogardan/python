'''
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру, например словарь.
6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
'''

class OfficeEquipment:
    type = 'base'

    def __init__(self, price, color, producer):
        self.price = price
        self.color = color
        self.producer = producer

    def get_params(self):
        return {
            'price': self.price,
            'color': self.color,
            'producer': self.producer
        }

class Printer(OfficeEquipment):
    type = 'printer'

    def set_multicolored(self, is_multicolored):
        self.multicolored = is_multicolored

    def get_params(self):
        params = super().get_params()
        params['is_multicolored'] = self.multicolored
        return params

class Scanner(OfficeEquipment):
    type = 'scanner'

    def set_mfu(self, is_mfu):
        self.mfu = is_mfu

    def get_params(self):
        params = super().get_params()
        params['is_mfu'] = self.mfu
        return params

class Copier(OfficeEquipment):
    type = 'copier'

    def set_standalone(self, is_standalone):
        self.standalone = is_standalone

    def get_params(self):
        params = super().get_params()
        params['is_standalone'] = self.standalone
        return params

class Warehouse:

    equipment = {
        'IT': {'max': 3, 'items': []},
        'BUH': {'max': 5, 'items': []},
        'Administration': {'max': 2, 'items': []},
        'Sklad': {'max': 99, 'items': []}
    }

    """
    Добавление оборудования происходит поединично.
    """
    def send_item_to_warehouse(self, item: OfficeEquipment):
        if item.type == 'printer':
            department = 'BUH'
        elif item.type == 'scanner':
            department = 'Administration'
        elif item.type == 'printer':
            department = 'IT'
        else:
            department = 'Sklad'

        check_result = self.check_equipment(department, item)
        if not check_result:
            raise OverflowError(f'Оборудование типа {item.type} для отдела {department} уже укомплектовано')

        self.equipment[department]['items'].append(item)

    def get_warehouse_items(self):
        return self.equipment

    def check_equipment(self, department, item: OfficeEquipment):
        if len(self.equipment[department]['items']) < self.equipment[department]['max']:
            return True
        else:
            return False


warehouse = Warehouse()
try:
    warehouse.send_item_to_warehouse(Printer(1000, 'white', 'Xerox'))
    warehouse.send_item_to_warehouse(Printer(3000, 'yellow', 'Brother'))
    warehouse.send_item_to_warehouse(Scanner(15000, 'black', 'HP'))
    warehouse.send_item_to_warehouse(Copier(1000, 'white', 'Xerox'))
    warehouse.send_item_to_warehouse(OfficeEquipment(1000, 'white', 'KY'))
except Exception as err:
    print(err)

print(warehouse.get_warehouse_items())
