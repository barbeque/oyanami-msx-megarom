ROM_SIZE = int(4 * 1024 * (1024 // 8)) # 4 mbit
CYCLE_SIZE = int(ROM_SIZE // 256)

value = int(0)

buf = [0x00] * ROM_SIZE

while value < ROM_SIZE:
    buf[value] = value // CYCLE_SIZE
    value += 1

assert(len(buf) == ROM_SIZE)

with open('dummy.rom', 'wb') as f:
    f.write(bytes(buf))
