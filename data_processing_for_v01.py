
import re
import matplotlib.pyplot as plt
import os
import pdb

# srcs = ['ba133', 'co60', 'cs137', 'th232' ]
# srcs = ['am232','ra226', 'co57', 'cs137', 'ba133','co60','th232' ]
srcs = ['am232', 'cs137', 'ba133','co60']
measure_time_minute = 2 # 2 minutes

# Pharse 0: Extract spectrum from raw spc file
if 0:
    input_dir = os.path.join('sprd_dataset_v01','fresh_data')
    output_dir = os.path.join('sprd_dataset_v01','extracted')
    os.makedirs(output_dir, exist_ok=True)
    pattern  = re.compile(r'Spc: ')
    for src in srcs:
        try:
            with open(os.path.join(input_dir,f'{src}_fresh.txt'),'r') as rFile:
                print(f"Extracting {src}...")
                # with open(f'{src}_spc_extracted.txt', 'w') as wFile:
                with open (os.path.join(output_dir,f'{src}_extracted_raw_data.txt'), 'w') as wFile:
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

# Pharse 1: compress 60 samples --> 1 sample
# 5 mins dataset

tmp = []
tmp_spc = []
input_dir = os.path.join('sprd_dataset_v01','extracted')
output_dir = os.path.join('data','extracted')
for src in srcs:
    try:
        with open(os.path.join(input_dir,f'{src}_extracted_raw_data.txt'), 'r') as rFile:
            with open (os.path.join(output_dir,f'{src}_{measure_time_minute}mins_dataset.txt'), 'w') as wFile:
                for idx,line in enumerate(rFile):
                    tmp = line.split(',')
                    # Remove '\n'
                    tmp[len(tmp)-1] = tmp[len(tmp)-1].strip()

                    tmp_spc.append([float(i) for i in tmp])
                    # agregate every measure_time_minute*60 samples (120s now)
                    if (idx + 1) % (measure_time_minute*60) == 0 and idx != 0:
                        avg = list(sum(item) for item in zip(*tmp_spc))
                        wFile.writelines(','.join(map(str, avg)) + '\n')
                        tmp_spc = []

    except FileNotFoundError:
        print(f"File {src}_spc_extracted.txt not found.")
        continue

    except Exception as e:
        print(f"An error occurred: {e}")
        continue

    finally:
        print(f"Compressed {src} data successfully")
        rFile.close()
        wFile.close()

