
import re
import matplotlib.pyplot as plt
import os
import pdb

# srcs = ['ba133', 'co60', 'cs137', 'th232' ]
# srcs = ['am232','ra226', 'co57', 'cs137', 'ba133','co60','th232' ]
srcs = ['th232', 'ra226']
measure_time_minute = '2mins' # seconds

# Pharse 0: Extract spectrum from raw spc file
if 1:
    input_dir = os.path.join('sprd_dataset_v02','fresh_data')
    output_dir = os.path.join('data','extracted')
    os.makedirs(output_dir, exist_ok=True)
    pattern  = re.compile(r'Spc: ')
    for src in srcs:
        try:
            with open(os.path.join(input_dir,f'{src}_fresh_spc.txt'),'r') as rFile:
                print(f"Extracting {src}...")
                # with open(f'{src}_spc_extracted.txt', 'w') as wFile:
                with open (os.path.join(output_dir,f'{src}_{measure_time_minute}_dataset.txt'), 'w') as wFile:
                    for  line in rFile:
                        m = re.search(pattern, line)
                        wFile.writelines(line[m.end():])
        except FileNotFoundError:
            print(f"File {src}.txt not found.")
            continue
        except Exception as e:
            print(f"An error occurred: {e}")
            continue
        finally:
            print(f"Extracted {src} data successfully")
else:
    pass
