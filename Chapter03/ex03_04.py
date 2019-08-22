
#!/usr/bin/python

transports=["bus","taxi","bike","boat"]
transports.append("airplane")
print("I would like go out by " + transports[0])
print(transports)
transports.insert(0,"train")
print("I would like go out by " + transports[0])
print(transports)
del transports[2]
print("I would like go out by " + transports[0])
print(transports)
transports.pop(2)
print("I would like go out by " + transports[0])
print(transports)