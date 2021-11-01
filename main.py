# This is an example file to present the basic functionality of AXOtest.

# to use AXOtest, import it
import axotest

# for each test, create a class from axotest.Unit
class Homepage(axotest.Unit):
  def __init__(self):
    # define a name and a failure message
    self.name = "Homepage test"
    self.failure = "failed"
    
  # this function is being run by axotest
  def test(self):
    X, Y = 21, 42
    # assert
    assert X*2 == Y

class Faculty(axotest.Unit):
  def __init__(self):
    self.name = "Faculty test"
    self.failure = "failed"
  def faculty(self, val):
    return (1 if val == 1 else val * self.faculty(val-1))
  def test(self):
    assert self.faculty(100) == 100

class Internet(axotest.Unit):
  def __init__(self, site):
    self.name = "Connection to " + site
    self.failure = "no connection"
    self.site = site
  def test(self):
    import requests
    try:
      requests.get(self.site, timeout=2)
    except Exception:
      assert False

# at the end, run axotest.run_test passing a list of all objects to run them
axotest.run_tests([
  Homepage(),
  Faculty(),
  Internet("http://1.1.1.1"),
  Internet("http://8.8.8.8"),
  Internet("Lollipop"),
  Internet("https://www.axome.de/")
])

# that's it