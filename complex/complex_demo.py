import complex.complex_pb2 as complex_pb2

complex_message = complex_pb2.ComplexMessage()

one_dummy = complex_message.one_dummy
one_dummy.id = 123
one_dummy.name = "first dummy"

multiple_dummy = complex_message.multiple_dummy.add()
multiple_dummy.id =123
multiple_dummy.name = "second dummy"

complex_message.multiple_dummy.add(id=456, name="third dummy")

third_dummy = complex_pb2.DummyMessage()
third_dummy.id = 111
third_dummy.name = "third dummy"

complex_message.multiple_dummy.extend([third_dummy])
third_dummy.id=999
 
print(third_dummy)
print(complex_message)
