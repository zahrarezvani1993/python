import os
import shutil

class file_management():

    def create_file(self,fname,valus):
        with open(fname, "w") as f:
            f.write(valus)

    def create_directory(self,dname):
        if not os.path.exists(dname):
            os.makedirs(dname)

    def remove_file(self,fname):
        os.remove(fname)

    def remove_directory(self,dname):
        shutil.rmtree(dname)

    def list_directory_file(self,address):
        files = os.listdir(address)
        print(files)
    