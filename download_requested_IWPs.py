import os, glob, shutil

def download_requested_data(id_list, folders, dest):
    """
    This function will automatically download the IWP shapefiles for a given data request. This is
    necessary since the shapefiles are all distributed throughout their own individual sub-folders and makes manual
    downloading very time-consuming. The user will give a .txt file holding the scene IDs that fall within the
    requested AOI (can quickly be generated manually within GIS software). The user should also know which particular
    grid selection areas fall within the AOI and give a list of the corresponding directories. The function will then
    automatically copy the IWP shapefiles for each scene ID for each directory into a destination folder.

    id_list: string = Filename of .txt file that contains scene ID strings for each scene that falls within the
        requested AOI. Each row in the .txt file holds one scene ID.
        (e.g., WV03_20200817230230_1040010060527C00_20AUG17230230-M1BS-504682687080_01_P001)
    folders: [string] = List of directories that hold the IWP shapefiles for a given grid selection area
        (e.g., ["F:\high\alaska\178_179_180_iwp", 'F:\high\alaska\146_157_iwp', 'F:\high\alaska\167_168_iwp']
    dest: string = Destination directory to which the selected IWP shapefiles will be moved.

    """

    footprints = []

    for line in open(id_list, 'r'):
        line = line[:-1]
        footprints.append(line+'_u16rf3413_pansh')

    count = 0

    for folder in folders:
        for root, dirs, files in os.walk(folder):
            for name in files:
                (base, ext) = os.path.splitext(name)
                if ext in ('.shp', '.dbf', '.prj', '.shx'):
                    full_name = os.path.join(root, name)
                    if base in footprints:
                        count += 1
                        shutil.copy2(full_name, dest)
                        print(f"{full_name}")


folders = [r'F:\pan_arctic_master_copy\high\alaska\178_179_180_iwp']
dest = r"D:\data_requests\ronnie_request\AOI_IWPs"

download_requested_data(r"D:\data_requests\ronnie_request\AOI_sceneIDs.txt", folders, dest)

print(count)