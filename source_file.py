import os
import shutil
from datetime import datetime
import argparse

def sync_folders():
   
   parser = argparse.ArgumentParser(description='Syncronization between two folders')
   parser.add_argument('source_folder', help='path to the source folder')
   parser.add_argument('replica_folder', help='path to the destination folder')
   parser.add_argument('log_file', help='path to log file')

   args = parser.parse_args()
   src = args.source_folder
   dst = args.replica_folder
   log_file = args.log_file

   if not os.path.exists(src):
    print("Source folder does not exist.")
    exit()

   if not os.path.exists(dst):
    os.makedirs(dst)
    print("Replica folder created.")

   for item in os.listdir(src):
    source_path = os.path.join(src, item)
    replica_path = os.path.join(dst, item)
    
    shutil.copy2(source_path, replica_path)

    with open(log_file, "a") as log:
     log.write(f"{datetime.now()}: Copied {source_path} to {replica_path}\n")
    print(f'{datetime.now()}: Copied {item}\n' )

if __name__ == "__main__":
    sync_folders()