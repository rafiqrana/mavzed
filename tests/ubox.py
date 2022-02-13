from serial import Serial
from pyubx2 import UBXReader


stream = Serial('COM8', 9600, timeout=3)
ubr = UBXReader(stream)
(raw_data, parsed_data) = ubr.read()
print(parsed_data)