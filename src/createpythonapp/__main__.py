import os
import sys

from helpers.fshelper import FsHelper
from projcreator import ProjectCreator


helpMsg = '''options:
          -name: project name(mandatory)
          -template: folder structure,  available templates are:
            -default: recommended structure(used if no parameter is specified)          
            -pypa:python project authority model
            -empty: empty project with default main file
          -path:  project location. if no specified, current location is used
          -help: help'''
useMsg = "create-python-app -name [projectName] -template [empty|pypa|default] -path [projectPath]"


def wordIsOption(word): 
    return '-' in word

def isValidTemplateOption(option):
    if option == 'pypa' or option=='default' or option=='empty':
        return True
    else:
        return False

def processInput(arguments, projectTemplate, basePath):
    """ parse the received parameters and use only those that are valid and correct"""
    if("-help" in arguments):
        print(useMsg)
        print(helpMsg)
    else:
        if "-name" in arguments:
            nameIndex = arguments.index("-name")
            if len(arguments) >=2 and not wordIsOption(arguments[nameIndex+1]):
                projectName = arguments[nameIndex + 1]
                if("-template" in arguments):
                    templateIndex = arguments.index("-template")
                    if(len(arguments) >= templateIndex + 1):
                        projectTemplate = arguments[templateIndex + 1]
                    if not isValidTemplateOption(projectTemplate):
                        print('invalid template name, valid options are: default, empty, pypa')
                        return
                if "-path" in arguments:
                    pathIndex = arguments.index("-path")
                    if(len(arguments) >= arguments.index("-path")):
                        basePath = arguments[pathIndex + 1]
                
                fshelper = FsHelper()
                pcreator = ProjectCreator(fshelper, basePath)
                pcreator.createProject(projectName, projectTemplate)
            else:
                print(useMsg)
        else:
            print(useMsg)


basePath = os.getcwd()
arguments = sys.argv
projectTemplate = 'default'
projectPath = basePath
processInput(arguments, projectTemplate, basePath)
