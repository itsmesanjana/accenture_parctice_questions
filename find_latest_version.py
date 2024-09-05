def find_latest_version(files):
    latest_version=-1
    for file in files:
        # if file.startswith("File_") and file[5:].isdigit():
        parts=file.split('_')
        if (len(parts)==2) and parts[0]=="File" and parts[1].isdigit():         
            latest_version=max(latest_version,int(parts[1]))
    return latest_version
files=["File_1","File_2","File_3","File_0","File_invalid"]
print(find_latest_version(files))  # Output: 10