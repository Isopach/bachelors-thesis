import re
import base64

# Read File
match = re.findall(r'CDATA\[\w+\==',open('xmlfilename','r').read())
# Removes string unused in Base64 code (but used for regex)
match = ([s.replace('CDATA[', '') for s in match])
# Flattens the list by joining elements
match = ' '.join(match)
# Decode into text
match = base64.b64decode(match)
# Finds value of Content-Length
match = re.findall(r'Content-Length: \d+',match)
# Extracts Content Length
match = ([s.replace('Content-Length: ', '') for s in match])
# Converts to integer
match = [int(x) for x in match]
# Sums all content length
count = sum(match)
print count
