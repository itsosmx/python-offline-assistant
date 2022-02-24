from json import load
from random import choice
# get response and keys from dataset
def dataset(key):
  """
  returns `keys`, `responses`
  """
  with open('dataset.json') as file:
    data = load(file)
    keys = data[key]['keys']
    responses = data[key]['responses']
    return keys, choice(responses)
  
# matchs open key
def isWake(text):
  if not text: return False
  isword = 0
  keys, _ = dataset('wake')
  for keyword in keys:
    if keyword in text:
      isword = 1
      return True
  if not isword: return False