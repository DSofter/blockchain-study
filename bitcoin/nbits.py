from binascii import hexlify

block_hash = '000000000000000000c342e73ca0a4ebc85753461611f5c08ca6dba345ed8d6a'
nbits_int = 402705995

def get_target_hex_string_from_nbits(nbits_int):
  # nbits_int: 402705995

  nbits_bytes_little_endian = nbits_int.to_bytes(4, byteorder='little')
  # b'K\xce\x00\x18'

  exponent = nbits_bytes_little_endian[-1:][0]
  # 24

  significand = int.from_bytes(nbits_bytes_little_endian[:-1], byteorder='little')
  # 52811

  target = significand*256**(exponent - 3)
  # 19758940920085072387393228723348383373068660102939017216

  target_hex_string = hexlify(target.to_bytes(32, byteorder='big')).decode()
  # 000000000000000000ce4b000000000000000000000000000000000000000000

  return target_hex_string

def main():
  print(get_target_hex_string_from_nbits(nbits_int))

if __name__ == '__main__':
  main()
