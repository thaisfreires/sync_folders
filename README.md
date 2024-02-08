## Syncronization program

This program is a one-way synchronization tool designed to replicate files from a source folder to a replica folder. It operates by copying any new or updated files from the source folder to the replica folder, ensuring that the replica folder mirrors the contents of the source folder. Additionally, it logs each copying operation to a specified log file, providing a record of the synchronization process.

##Requirements

Python3

##Libraries

`os`
`shutil`
`datetime`
`argparse`

##Usage
```bash
python main.py "path/to/source_folder" "path/to/replica_folder" "path/to/log_file"
```
