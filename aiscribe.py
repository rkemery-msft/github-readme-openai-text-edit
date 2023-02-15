import os
import openai
import time
import sys
from datetime import datetime
from pathlib import Path

var_model = "text-davinci-edit-001"
var_instruction = "Make this more concise"
var_temp = 0
var_sleep = 30
readme_file = "README.md"
results = "results.txt"
results_path = os.getcwd() + "/" + results
dt = datetime.now()

# Check if results.txt exists
path = Path(results_path)
if path.is_file():
  while True or False:
    try:
      answer = str(input(f'The file {results} exists. Delete it? [y]es or [n]o: '))
      if answer == "y":
        print(f'Deleted {results}')
        os.remove(results_path)
        break;
      if answer == "n":
        print(f'Leaving {results} in directory with a timestamp.')
        os.rename(results_path, results_path + '_' + str(datetime.timestamp(dt)))
        break;
      else:
        print(f'Provide a y for yes or n for no to continue...')
    except ValueError:
      print(f'Provide a y for yes or n for no to continue...')
      continue

# Set up the OpenAI API client and read file
openai.api_key = os.environ.get('OPENAI_API_KEY')

result = []

def OpenReadme():
  with open(readme_file, 'rt') as f:
      data = f.readlines()
  for line in data:
    if '**' in line:
      result.append(line.strip())
  for i in range(len(result)):
    output = openai.Edit.create(
      model=var_model,
      temperature=var_temp,
      input=str(result[i]),
      instruction=var_instruction)
    sys.stdout = open(results,'a')
    print(output.choices[0].text)
    time.sleep(var_sleep)

OpenReadme()