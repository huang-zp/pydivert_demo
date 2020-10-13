import pydivert

with pydivert.WinDivert("tcp.PayloadLength > 0") as w:
    for packet in w:
        if packet.src_addr == '127.0.0.1' and packet.src_port == 5000:

            if b'Hello, World!' in packet.payload:
                str_data = packet.payload.decode('utf-8').replace('Hello, World!', 'Hello, Hacker!')
                packet.payload = str_data.encode('utf-8')
        w.send(packet)






