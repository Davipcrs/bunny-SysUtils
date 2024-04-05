# ============================================
# Easy Backup files to a file server!
# Author: Davipcrs
# Date: 02/04/2023
# ============================================

import os
from threading import Thread
from multiprocessing import Process
from zipfile import ZipFile, ZIP_DEFLATED
import modules.confMgr.load_conf_file as conf


class BackupUtils():
    def __init__(self):
        self.currentFile = 0
        self.totalFiles = 0
        self.currentFileName = ""
        self.inProgress = True

    def _countFiles(self, input_dir: str):
        """Count the total file while zip"""
        totalFiles = 0
        for _, dirname, files in os.walk(input_dir):
            totalFiles += len(files) + len(dirname)

        self.totalFiles = totalFiles

    def _createZipFolder(self, input_dir: str, output_zip: str) -> str:
        """With a input dir and a output dir the function compress with compress level 9 all the files/folders in the entry directory and outputs the file"""
        with ZipFile(file=output_zip, mode="a", compression=ZIP_DEFLATED, compresslevel=9) as zipfolder:
            for base, _, files in os.walk(input_dir):
                # Base in the os.walk return function gives the "Father directory and its predecessors"
                # files in the os.walk return the "end file"
                for file in files:
                    filename = os.path.join(base, file)
                    self.currentFileName = filename
                    self.currentFile = self.currentFile + 1
                    zipfolder.write(filename)

            zipfolder.close()
            self.inProgress = False
        return output_zip

    def startBackup(self, input_dir: str, output_zip: str):
        """With a input dir and a output dir the function compress with compress level 9 all the files/folders in the entry directory and outputs the file"""
        Thread(target=self._countFiles, args=(input_dir,)).start()
        Thread(target=self._createZipFolder, args=(
            input_dir, output_zip)).start()

    def multiBackups(self):
        """
        Function to make Multiple zip folders backup simultaneously. 

        This function retrieves the folders from a json config file, for info see the confMgr Module.
        """
        procs = []
        data = conf.getBackupDataFromConf()
        folders = data.get("folders")
        outputs = data.get("outputs")
        if (len(folders) != len(outputs)):
            return "The 'folders' and  'outputs' aren't equals, so the zip folder can't be created"

        if (data.get("enable") == False):
            return "The Backup is disable"

        i = 0
        for i in range(len(folders)):
            proc = Process(target=self.startBackup,
                           args=(folders[i], outputs[i]))
            procs.append(proc)
            i = i + 1
        for proc in procs:
            proc.start()

        return procs


"""
## Example

bkp = BackupUtils()
bkp.startBackup("E:\\src", "E:\\Teste.zip")
while bkp.inProgress:
    time.sleep(0.2)
    aux = bkp.totalFiles - bkp.currentFile
    print("Remaning files to backup: " + str(aux))

"""
