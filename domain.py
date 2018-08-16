import uuid


class Domain:
    def __init__(self, id=None, name=None):
        self.id = id
        self.name = name
        # TODO: do some input validation
        self.mac_address = self.generate_mac_address()

    def generate_mac_address(self, num_of_ids=10):
        for i in range(number_of_ids):
            id_hex = self.int_to_hex(self.id)
            uuid_hex = self.generate_uuid_32(self.id, self.name, 10)
            #append
        return self.format_mac_address(id_hex, uuid_hex)

    def int_to_hex(self, my_id):
        # TODO: is it better to remove id argument, and refer to self.id instead?
        # formats id as hex with leading zeroes (if applicable)
        return '{0:04X}'.format(my_id)

    def format_mac_address(self, id_hex, uuid_hex):
        # might be unnecessary
        pass

