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
        self.currentFile = []  # Refatorar para um Array
        self.totalFiles = []  # Refatorar para um Array
        self.currentFileName = []  # Refatorar para um Array
        self.numJobs = 0
        self.inProgress = True

    def _arrayTotalFilesCounter(self, input_dir: str, job_num: int):
        self.currentFile.append(0)
        self.totalFiles.append(0)
        self.currentFileName.append("")
        f_job = self._countFiles(input_dir)
        # print("Saiu, Jobnum:" + str(job_num) + " files: " + str(f_job))
        self.totalFiles[job_num] = f_job

    def _countFiles(self, input_dir: str):
        """Count the total file while zip"""
        # Refatorar para um Array
        totalFiles = 0
        for _, dirname, files in os.walk(input_dir):
            totalFiles += len(files) + len(dirname)
        return totalFiles

    def _createZipFolder(self, input_dir: str, output_zip: str, job_num: int = 0) -> str:
        """With a input dir and a output dir the function compress with compress level 9 all the files/folders in the entry directory and outputs the file"""
        with ZipFile(file=output_zip, mode="a", compression=ZIP_DEFLATED, compresslevel=9) as zipfolder:
            for base, _, files in os.walk(input_dir):
                # Base in the os.walk return function gives the "Father directory and its predecessors"
                # files in the os.walk return the "end file"
                for file in files:
                    filename = os.path.join(base, file)
                    self.currentFileName[job_num] = filename
                    self.currentFile[job_num] = self.currentFile[job_num] + 1
                    zipfolder.write(filename)

            zipfolder.close()
            self.inProgress = False
        return output_zip

    def startBackup(self, input_dir: str, output_zip: str, job_num: int = 0):
        """With a input dir and a output dir the function compress with compress level 9 all the files/folders in the entry directory and outputs the file"""

        # Thread(target=self._countFiles, args=(input_dir, job_num,)).start()
        self._createZipFolder(input_dir, output_zip, job_num)

    def multiBackups(self):
        """
        Function to make Multiple zip folders backup simultaneously. 

        This function retrieves the folders from a json config file, for info see the confMgr Module.
        """
        procs = []  # Multiprocess ID arrays
        data_array = []
        data = conf.getBackupDataFromConf()  # Load Conf file
        folders = data.get("folders")  # Retrieve Data
        outputs = data.get("outputs")  # Retrieve Data

        # Error Checks:
        if (len(folders) != len(outputs)):
            return "The 'folders' and  'outputs' aren't equals, so the zip folder can't be created"

        if (data.get("enable") == False):
            return "The Backup is disable"

        i = 0  # Process "ID"
        for i in range(len(folders)):
            # Crete the process
            proc = Process(target=self.startBackup,
                           args=(folders[i], outputs[i], i))

            self._arrayTotalFilesCounter(folders[i], i)  # Calls The Counter
            procs.append(proc)  # Process Array
            data_array.append([folders[i], outputs[i], i])  # Data Array
            i = i + 1
        self.numJobs = i
        for proc in procs:
            # Start The Process
            proc.start()

        return data, procs


"""
## Example

bkp = BackupUtils()
bkp.startBackup("E:\\src", "E:\\Teste.zip")
while bkp.inProgress:
    time.sleep(0.2)
    aux = bkp.totalFiles - bkp.currentFile
    print("Remaning files to backup: " + str(aux))

"""
