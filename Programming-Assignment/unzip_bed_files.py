#!/usr/bin/env python3

import os
import gzip
import shutil
import glob

def unzip_bed_files(source_dir="data", target_dir="."):
    """
    Unzip all .bed.gz files from source_dir to target_dir
    """
    os.makedirs(target_dir, exist_ok=True)
    
    bed_files = glob.glob(os.path.join(source_dir, "*.bed.gz"))
    
    if not bed_files:
        print(f"No .bed.gz files found in {source_dir}")
        return
    
    for gz_file in bed_files:
        base_filename = os.path.basename(gz_file)[:-3]  # Remove .gz
        output_path = os.path.join(target_dir, base_filename)
        
        print(f"Extracting {gz_file} to {output_path}")
        
        try:
            with gzip.open(gz_file, 'rb') as f_in:
                with open(output_path, 'wb') as f_out:
                    shutil.copyfileobj(f_in, f_out)
            print(f"Successfully extracted {base_filename}")
        except Exception as e:
            print(f"Error extracting {gz_file}: {e}")

if __name__ == "__main__":
    unzip_bed_files()
    print("Extraction complete")
