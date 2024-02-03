import inquirer
import subprocess

questions = [
    inquirer.List('script',
                  message="Which script would you like to run?",
                  choices=['Import', 'Generate', 'Clean'],
                  ),
]

answers = inquirer.prompt(questions)

# Running the selected script
if answers['script'] == 'Import':
    subprocess.run(["python3", "script.py"])
elif answers['script'] == 'Generate':
    subprocess.run(["python3", "generator.py"])
elif answers['script'] == 'Clean':
    subprocess.run(["python3", "clean.py"])
