# presentation in "main.py"

class Unit:
  def __init__(self, name, failure="failed"):
    self.name = name
    self.failur
  def test(self):
    pass

class color:
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

def run_tests(units):
  print("--- Running tests... ---")
  for x, i in enumerate(units):
    try:
      i.test()
      print("Test "+str(x+1)+" ["+color.BOLD+i.name+color.ENDC+"]: "+color.BOLD+color.OKGREEN+"passed"+color.ENDC)
    except AssertionError:
      print("Test "+str(x+1)+" ["+color.BOLD+i.name+color.ENDC+"]: "+color.BOLD+color.FAIL+i.failure+color.ENDC)
  print("--- "+color.BOLD+str(len(units))+" tests ran"+color.ENDC+" ---")