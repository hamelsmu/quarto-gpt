import os
import subprocess
import math
from glob import glob

# Clone the GitHub repository
repo_url = 'https://github.com/quarto-dev/quarto-web.git'
repo_dir = 'quarto-web'
if not os.path.isdir(repo_dir):
    subprocess.run(['git', 'clone', '--depth', '1', repo_url], check=True)

# Recursively find all .qmd files
qmd_files = glob(f'{repo_dir}/**/*.qmd', recursive=True)

# Calculate the number of files per chunk
files_per_chunk = math.ceil(len(qmd_files) / 10)

for i in range(10):
    # Determine the output file name
    output_file = f'concatenated_{i+1}.md'
    
    # Open the output file
    with open(output_file, 'w') as f_out:
        # Calculate the slice of files for this chunk
        start_idx = i * files_per_chunk
        end_idx = start_idx + files_per_chunk
        for file in qmd_files[start_idx:end_idx]:
            # Write the header with the path and name of the file
            f_out.write(f'# {file}\n\n')
            
            # Write the content of the .qmd file
            with open(file, 'r') as f_in:
                f_out.write(f_in.read())
            
            # Write a separator newline
            f_out.write('\n\n')

print('Concatenation complete.')
