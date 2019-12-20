#!/usr/bin/env python

import traceback
from sys import argv, stderr
import imp

#**************************************************************************
#STEP 1. READ CONFIGURATION AND PARSE INPUT FILES
#
# DO NOT CHANGE THIS CODE
#**************************************************************************
SPECIE      = argv[1]
ROOT_DIR    = argv[2].rstrip("/") + "/"      #Should be src/AdminTools
DESTINATION = argv[3].rstrip("/") + "/"

COMMON_BUILD_DB_TOOLS = imp.load_source('common_build_database', ROOT_DIR + "scripts/common_build_database.py")
COMMON_BUILD_DB_TOOLS.SPECIE= SPECIE
COMMON_BUILD_DB_TOOLS.EXTERNAL_RESOURCES = imp.load_source('download_conf',  ROOT_DIR + "scripts/" + SPECIE + "_resources/download_conf.py").EXTERNAL_RESOURCES
COMMON_BUILD_DB_TOOLS.COMMON_RESOURCES = imp.load_source('download_conf',  ROOT_DIR + "scripts/common_resources/download_conf.py").EXTERNAL_RESOURCES

SERVER_SETTINGS = imp.load_source('serverconf.py',  ROOT_DIR + "../conf/serverconf.py")


#**************************************************************************
# CHANGE THE CODE FROM HERE
#
# STEP 2. DOWNLOAD FILES
#**************************************************************************
try:

    #**************************************************************************
    #STEP 2.1 GET MapMan NCBI ID -> MapMan GENE ID
    # **************************************************************************
    resource = COMMON_BUILD_DB_TOOLS.EXTERNAL_RESOURCES.get("mapman_kegg")[0]
    COMMON_BUILD_DB_TOOLS.downloadFile(resource.get("url"), resource.get("file"), DESTINATION + resource.get("output"), SERVER_SETTINGS.DOWNLOAD_DELAY_1, SERVER_SETTINGS.MAX_TRIES_1)

    # **************************************************************************
    # STEP 2.1 GET MapMan GENE ID -> MAPMAN FEATURE ID
    # **************************************************************************
    resource = COMMON_BUILD_DB_TOOLS.EXTERNAL_RESOURCES.get("mapman_gene")[0]
    COMMON_BUILD_DB_TOOLS.downloadFile(resource.get("url"), resource.get("file"), DESTINATION + resource.get("output"),
                                       SERVER_SETTINGS.DOWNLOAD_DELAY_1, SERVER_SETTINGS.MAX_TRIES_1)


    #**************************************************************************
    #STEP 2.1 GET MapMan pathways
    # **************************************************************************
    resource = COMMON_BUILD_DB_TOOLS.EXTERNAL_RESOURCES.get("mapman_pathways")[0]
    COMMON_BUILD_DB_TOOLS.downloadFile(resource.get("url"), resource.get("file"), DESTINATION + resource.get("output"), SERVER_SETTINGS.DOWNLOAD_DELAY_1, SERVER_SETTINGS.MAX_TRIES_1)

    #**************************************************************************
    #STEP 2.1 GET MapMan pathways classification
    # **************************************************************************
    resource = COMMON_BUILD_DB_TOOLS.EXTERNAL_RESOURCES.get("mapman_classification")[0]
    COMMON_BUILD_DB_TOOLS.downloadFile(resource.get("url"), resource.get("file"), DESTINATION + resource.get("output"), SERVER_SETTINGS.DOWNLOAD_DELAY_1, SERVER_SETTINGS.MAX_TRIES_1)


   #**************************************************************************
    #STEP 2.1 GET MapMan compound dataset
    # **************************************************************************
    resource = COMMON_BUILD_DB_TOOLS.COMMON_RESOURCES.get("mapman").get("metabolites")
    COMMON_BUILD_DB_TOOLS.downloadFile(resource.get("url"), resource.get("file"), DESTINATION + resource.get("output"), SERVER_SETTINGS.DOWNLOAD_DELAY_1, SERVER_SETTINGS.MAX_TRIES_1)


except Exception as ex:
    stderr.write("FAILED WHILE DOWNLOADING DATA " + str(ex))
    traceback.print_exc(file=stderr)
    exit(1)

exit(0)
