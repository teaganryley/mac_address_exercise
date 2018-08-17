import uuid


class Domain:
    def __init__(self, id=0, name=None):
        self.id = id
        self.name = name
        self.mac_addresses = []

    def generate_mac_address(self, num_of_ids=10):
        for i in range(num_of_ids):
            id_hex = self.int_to_hex(self.id)
            uuid_hex = self.generate_uuid4()
            self.mac_addresses.append(self.format_mac_address(id_hex, uuid_hex))

    def int_to_hex(self, my_id=0):
        # formats id as hex with leading zeroes (if applicable)
        return '{0:04X}'.format(my_id)

    def generate_uuid4(self):
        # generates uuid version 4 and slices the first 32 bits
        return str(uuid.uuid4())[:8]

    def format_mac_address(self, id_hex, uuid_hex):
        # concatenates domain id and uuid4, then formats with colon
        temp = id_hex + uuid_hex
        mac = ':'.join(temp[i:i+2] for i in range(0, len(temp), 2))
        return mac

