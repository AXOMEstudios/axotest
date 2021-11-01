import axotest

class Homepage(axotest.Unit):
  def __init__(self):
    self.name = "Homepage test"
    self.failure = "failed"
  def test(self):
    X, Y = 21, 42
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

axotest.run_tests([
  Homepage(),
  Faculty(),
  Internet("http://1.1.1.1"),
  Internet("http://8.8.8.8"),
  Internet("Lollipop"),
  Internet("https://www.axome.de/")
])