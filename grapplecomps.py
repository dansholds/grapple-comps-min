import inquirer
import subprocess
#list to be presented when starting script
questions = [
    inquirer.List('script',
                  message="Which script would you like to run?",
                  choices=['Import UK', 'Import US', 'Generate', 'Clean'],
                  ),
]

answers = inquirer.prompt(questions)

# Running the selected script
if answers['script'] == 'Import UK':
    subprocess.run(["python3", "import_uk.py"])
elif answers['script'] == 'Import US':
    subprocess.run(["python3", "import_us.py"])
elif answers['script'] == 'Generate':
    subprocess.run(["python3", "generator.py"])
elif answers['script'] == 'Clean':
    subprocess.run(["python3", "clean.py"])
