# Dataset-Nuclide

SPRD-based gamma spectroscopy datasets and simple processing utilities for building training and test splits. This repo contains raw and lightly processed spectra for multiple isotopes across two dataset vintages (v01 and v02), plus small Python scripts to extract spectra, aggregate by time, and split into train/test files.

**Repository Structure**
- `sprd_dataset_v01/`: First dataset vintage with raw, fresh, and extracted data.
- `sprd_dataset_v02/`: Second dataset vintage with raw and fresh data; per‑version README inside.
- `data_processing_for_v01.py`: Extracts and aggregates v01 spectra into 2‑minute samples.
- `data_l2l_processing_for_v02.py`: Extracts spectra from v02 `.spc` logs into per‑source files.
- `gen_training_test_set.py`: Splits extracted datasets into training and testing subsets.

**Datasets**
- `sprd_dataset_v01/raw_data/`: Original text logs per isotope (e.g., `cs137.txt`).
- `sprd_dataset_v01/fresh_data/`: Newer/rawer logs with `Spc:` fields (e.g., `co60_fresh.txt`).
- `sprd_dataset_v01/extracted/`: Line‑by‑line spectra extracted from fresh logs.
- `sprd_dataset_v02/raw_data/`: Raw `.spc` text logs per isotope.
- `sprd_dataset_v02/fresh_data/`: Fresh logs used for extraction for v02.

Each raw or fresh line contains device metadata and a `Spc: v0,v1,...` CSV of channel counts. Scripts below strip to the spectrum and (optionally) time‑aggregate.

**Processing Scripts**
- `data_processing_for_v01.py`:
  - Phase 0 (toggle at top): extract `Spc:` CSV from `sprd_dataset_v01/fresh_data/*_fresh.txt` into `sprd_dataset_v01/extracted/*_extracted_raw_data.txt`.
  - Phase 1: aggregate every `measure_time_minute*60` samples (default 2 minutes) into a single CSV row and write to `data/extracted/{src}_{measure_time_minute}mins_dataset.txt`.

- `data_l2l_processing_for_v02.py`:
  - Extract `Spc:` CSV from `sprd_dataset_v02/fresh_data/*_fresh_spc.txt` and write to `data/extracted/{src}_{measure_time_minute}_dataset.txt` (default label `2mins`).
  - Adjust `srcs` and `measure_time_minute` at the top as needed.

- `gen_training_test_set.py`:
  - Reads `data/extracted/{src}_2mins_dataset.txt` for each source in `srcs`.
  - Writes first 501 lines to `data/training/{src}_training_dataset.txt` and next 100 to `data/testing/{src}_testing_dataset.txt`.

**Quick Start**
- Dependencies: Python 3.x, `matplotlib` (imported), plus standard library. No external data loaders required.
- Create outputs: scripts auto‑create `data/extracted`, `data/training`, and `data/testing` if missing.
- Typical workflow:
  1) For v01 data
     - Edit `srcs` as desired in `data_processing_for_v01.py`.
     - Enable Phase 0 (set the `if 0:` to `if 1:`) to extract fresh logs to `sprd_dataset_v01/extracted/`.
     - Run `python data_processing_for_v01.py` to produce aggregated `data/extracted/*_2mins_dataset.txt`.
  2) For v02 data
     - Edit `srcs` and `measure_time_minute` in `data_l2l_processing_for_v02.py`.
     - Run `python data_l2l_processing_for_v02.py` to produce `data/extracted/*_2mins_dataset.txt`.
  3) Split into train/test
     - Edit `srcs` in `gen_training_test_set.py` if needed.
     - Run `python gen_training_test_set.py` to populate `data/training/` and `data/testing/`.

**Notes**
- File naming: outputs use `{src}_{duration}_dataset.txt` to indicate source and aggregation window.
- Line format: each row is a comma‑separated spectrum vector (counts per channel).
- Script knobs: tune `srcs` lists and the aggregation window (`measure_time_minute`).
- Safety: scripts overwrite output files of the same name; back up if needed.

**Version READMEs**
- See `sprd_dataset_v02/README.md` for collection context specific to v02.
