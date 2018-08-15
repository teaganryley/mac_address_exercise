import uuid


class Domain:
    def __init__(self, id=None, name=None):
        self.id = id
        self.name = name
        self.mac_address = self.generate_mac_address()

    def generate_mac_address(self):
        id_hex = self.int_to_hex(self.id)
        uuid_hex = self.generate_uuid_32(self.id, self.name, 10)
        return self.format_mac_address(id_hex, uuid_hex)

    def int_to_hex(self, my_id):
        # TODO: is it better to remove id argument, and refer to self.id instead?
        # TODO: address leading zeroes
        return format(my_id, 'x')

    def generate_uuid_32(self, id, name, number_of_ids):
        for i in range(number_of_ids):
            pass
        pass

    def format_mac_address(self, id_hex, uuid_hex):
        pass
