import uuid


class Domain:
    def __init__(self, id=None, name=None):
        self.id = id
        self.name = name
        self.mac_address = self.generate_mac_address()

    def generate_mac_address(self, num_of_ids=10):
        mac_list = []
        for i in range(num_of_ids):
            id_hex = self.int_to_hex(self.id)
            uuid_hex = self.generate_uuid4()
            mac_list.append(self.format_mac_address(id_hex, uuid_hex))
        return mac_list

    def int_to_hex(self, my_id=0):
        # formats id as hex with leading zeroes (if applicable)
        return '{0:04X}'.format(my_id)

    def generate_uuid4(self):
        # generates uuid version 4 and slices the first 32 bits
        return str(uuid.uuid4())[:8]

    def format_mac_address(self, id_hex, uuid_hex):
        # concatenates domain id and uuid4, then formats with colon
        li = id_hex + uuid_hex
        mac = ':'.join((li[0:2], li[2:4], li[4:6], li[6:8], li[8:10], li[10:12]))
        return mac

