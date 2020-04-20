from datastructures.tree import Tree
from helpers.fshelper import FsHelper

README_TEXT=''
SETUP_TEXT=''
INITPY_TEXT=''

class ProjectCreator:
    def __init__(self, fsHelper, basePath):
        self.fsHelper = fsHelper
        self.basePath = basePath

    def iterateTree(self, treeNode):
        if treeNode.isFile:
            self.fsHelper.createFile(treeNode.name, treeNode.contents, "")
        else:
            self.fsHelper.createDirectory(treeNode.name)
            for child in treeNode.children:
                self.iterateTree(child)


    def createProject(self, projectName, projectTemplate):
        separator = ''
        if not self.basePath.endswith('/'):
            separator='/'
        projectPath = self.basePath + separator + projectName
        #self.fsHelper.createDirectory(projectPath)
        if projectTemplate == 'pypa':
            tree = Tree(projectPath, '', False,[
                    Tree(projectPath+'/data', '', False, []),
                    Tree(projectPath+'/tests','', False,[
                        Tree(projectPath+'/tests/__init__.py','#project tests', True, [])
                    ]),
                    Tree(projectPath+'/src', '', False,
                    [
                        Tree(projectPath+'/src/'+projectName,'',False,
                        [
                            Tree(projectPath+'/src/'+projectName+'/__init__.py','#entry point for app script', True, [])
                            
                        ])
                    ]),
                    Tree(projectPath+'/LICENSE.txt','Copyright (c)...', True,[]),
                    Tree(projectPath+'/MANIFEST.in','ManifestFile', True,[]),
                    Tree(projectPath+'/README.md','ManifestFile', True,[]),
                    ])
            self.iterateTree(tree)
        elif projectTemplate == 'default':
            tree = Tree(projectPath, '', False,[
                    Tree(projectPath+'/docs', '', False, []),
                    Tree(projectPath+'/tests','', False,[]),
                    Tree(projectPath+'/src', '', False,
                    [
                        Tree(projectPath+'/src/'+projectName,'',False,
                        [
                            Tree(projectPath+'/src/'+projectName+'/__init__.py','#entry point for app script', True, [])
                            
                        ])
                    ]),                   
                    Tree(projectPath+'/README.rst','', True,[]),
                    Tree(projectPath+'/setup.py','',True,[])
                    ])
            self.iterateTree(tree)
        else:
            tree = tree = Tree(projectPath, '', False,[Tree(projectPath+'/__main__.py','',True,[])])
            self.iterateTree(tree)