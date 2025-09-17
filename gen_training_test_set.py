
import re
import matplotlib.pyplot as plt
import os
import pdb


srcs = ['am232','ra226', 'cs137', 'ba133','co60','th232' ]

# Pharse 0: Extract spectrum from raw spc file
if 1:
    input_dir = os.path.join('data','extracted')
    output_train_dir = os.path.join('data','training')
    output_test_dir = os.path.join('data','testing')

    os.makedirs(output_train_dir, exist_ok=True)
    os.makedirs(output_test_dir, exist_ok=True)

    pattern  = re.compile(r'Spc: ')
    for src in srcs:
        try:
            with open(os.path.join(input_dir,f'{src}_2mins_dataset.txt'),'r') as rFile:
                print(f"Doing {src}...")
                # with open(f'{src}_spc_extracted.txt', 'w') as wFile:
                with open (os.path.join(output_train_dir,f'{src}_training_dataset.txt'), 'w') as wFile, \
                        open (os.path.join(output_test_dir,f'{src}_testing_dataset.txt'), 'w') as wFile2:
                    for  idx,line in enumerate(rFile):
                        if idx <= 500:
                            wFile.writelines(line)
                        elif idx > 500 and idx <= 600:
                            wFile2.writelines(line)
                        else:
                            break
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
