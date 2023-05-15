# -*- coding: utf-8 -*-
# @Time ： 2023/4/28 10:19
# @Auth ： JeremyChim
# @File ：script.py
# @IDE ：PyCharm
# @Github ：https://github.com/JeremyChim/Ethernet_Analysis_Tool

class udp_data():

    def __init__(self, udp_data):
        self.data = udp_data
        self._version = self.data[0:2]
        self._crc_len = self.data[2:4]
        self._packet_count = self.data[4:8]
        self._length = self.data[8:16]
        self._message_type = self.data[16:24]
        self._crc_value = self.data[24:32]
        self._frag_set = self.data[32:36]
        self._frag_offset = self.data[36:40]
        self._message_type_data = self.data[40:]

    def log(self):
        """输出报文的解析列表"""
        list = []
        list.append(self.version(self._version))
        list.append(self.crc_len(self._crc_len))
        list.append(self.packet_count(self._packet_count))
        list.append(self.length(self._length))
        list.append(self.message_type(self._message_type))
        list.append(self.crc_value(self._crc_value))
        list.append(self.frag_set(self._frag_set))
        list.append(self.frag_offset(self._frag_offset))

        return list

    def version(self, udp_data):
        """版本号，默认填充 0"""
        log = '版本号，默认填充 0'
        return udp_data, log

    def crc_len(self, udp_data):
        """CRC算法的长度 8/16/32，0x01表示8bit、0x10表示16bit、0x11 表示 32bit"""
        if udp_data == '01':
            log = 'CRC算法的长度: 8bit'
        elif udp_data == '10':
            log = 'CRC算法的长度: 16bit'
        elif udp_data == '11':
            log = 'CRC算法的长度: 32bit'
        return udp_data, log

    def packet_count(self, udp_data):
        """帧计数器，0 至 FFFF 循环计数"""
        log = f'帧计数器: 0x{udp_data}'
        return udp_data, log

    def length(self, udp_data):
        """数据帧的字节长度"""
        log = f'数据帧的字节长度: 0x{udp_data}'
        return udp_data, log

    def message_type(self, udp_data):
        """数据帧的数据类型，根据 message_type 的值，可区分数据包内容，比如 100ms 还是 200ms 的数"""
        log = f'数据帧的数据类型: 0x{udp_data}'
        return udp_data, log

    def crc_value(self, udp_data):
        """ 该帧的 crc 值，目前默认使用 32bit 算法，算法如下：
            CRC result width: 32 bits
            Polynomial: F4’AC’FB’13h
            Initial value: FFFFFFFFh
            Input data reflected: Yes
            Result data reflected: Yes
            XOR value: FFFFFFFFh """
        log = '该帧的 crc 值，目前默认使用 32bit 算法'
        return udp_data, log

    def frag_set(self, udp_data):
        """分片标志位，1 为分片，0 为未分片包"""
        log = '分片标志位，1 为分片，0 为未分片包'
        return udp_data, log

    def frag_offset(self, udp_data):
        """分片包偏移量，需除以 8，最大支持 512k 分片，在定义每包最大长度时，其长度需是 8 的整数倍"""
        log = '分片包偏移量，需除以 8，最大支持 512k 分片，在定义每包最大长度时，其长度需是 8 的整数倍'
        return udp_data, log

if __name__ == '__main__':
    a = '0011FFFF00000077000001465609d51b00000000'
    a = '001117560000000b000002719484712500000000001e63d40101000098acbf'
    b = udp_data(a)
    c = b.log()
    # c = b.crc_value('5609d51b')
    print(c)

    for i in range(len(c)):
        print(c[i][0]+',',c[i][1])