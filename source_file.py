import os
import shutil
from datetime import datetime
src = "source_folder"
dst = "replica_folder"
log_file = "log.txt"

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

