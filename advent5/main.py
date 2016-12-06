
input0 = "ffykfhsq"

input1 = "abc"

import hashlib

i = 0
password = list("--------")

while True:

    md5 = hashlib.md5(input0 + str(i)).hexdigest()

    if md5[:5] == "00000":

        sixth = md5[5]
        seventh = md5[6]

        if sixth in ['0','1','2','3','4','5','6','7']:
            if password[int(sixth)] == "-":
                password[int(sixth)] = seventh

        print md5
        print ''.join(password)

    if '-' not in password:
        break

    i += 1