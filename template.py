import os, sys
from pathlib import Path
import logging

while True:
    project_name = input('Enter your project name: ')
    if project_name != '':
        break

# src/__init__.py
# src/components/__init__.py

list_of_files = [
    f'{project_name}/__init__.py',
    f'{project_name}/components/__init__.py',
    f'{project_name}/config/__init__.py',
    f'{project_name}/constants/__init__.py',
    f'{project_name}/entity/__init__.py',
    f'{project_name}/exception/__init__.py',
    f'{project_name}/logger/__init__.py',
    f'{project_name}/pipeline/__init__.py',
    f'{project_name}/utils/__init__.py',
    f'config/config.yaml',
    f'schema.yaml',
    f'app.py',
    f'main.py',
    f'logs.py',
    f'exception.py',
    f'setup.py'

]


for filepath in list_of_files:
    filepath = Path(filepath)
    logging.info(f'{filepath} created')
    file_dir, filename = os.path.split(filepath)
    logging.info(f'directory name: {file_dir} | filename: {filename}')
    if file_dir != '':
        os.makedirs(file_dir, exist_ok=True)
    
    # logging.info(f'Does filepath exist: {os.path.exists(filepath)} | size: {os.path.getsize(filepath)}')

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
    
    else:
        logging.info(f'file already exists at : {filepath}')


