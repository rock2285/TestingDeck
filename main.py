import unittest
import tests
import card, deck
#app would go here

#code to run the tests; PyCharm does this automatically
#so this code could be removed in PyCharm

runner = unittest.TextTestRunner()
res=runner.run(tests.suite)
print(res)
print("*"*20)
for i in res.failures: print(i[1])