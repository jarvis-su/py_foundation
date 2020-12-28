import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of program')

message_str = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message_str:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

print(count)
for c in count:
    logging.debug('Count is ' + c)
