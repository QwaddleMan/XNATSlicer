# python
import os

# application
import slicer
import DICOMScalarVolumePlugin

# module
from Loader import *
from SlicerUtils import *
from XnatSlicerUtils import *

class Loader_Nifti(Loader_Images):
    """
    the loader for nifti files. will conduct the necessary steps
    to load nifti files into Slicer
    """
    def checkCache(self, fileUris):
        """
        checks nifti cache location for nifti files.
        nifti always gets downloaded no mater if its already there
        also doesnt use database to just dont use cache.
        """
        return False

    def load(self):
        """
        Main load method for downloading NIFTI files from an
        XNAT server and loading into Slicer
        """

        if not os.path.exists(self._dst) or not self.niiName:
            return

        SlicerUtils.loadNodeFromFile(self._dst)
        slicer.app.processEvents()




    def loadNiftisFromDatabase(self, niftiFiles):
        """
        Loads a nifti file from the nifti cache location
        into Slicer without prompting the user to input anything.
        The 'loadable' with the hightest priority has the highest
        file count.

        @param niftiFiles: The local niftiFiles to load.
        @type niftiFiles: list(str)
        """
        pass
