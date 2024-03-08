import os
import yaml
from src.text_summarizer.logging import logger
from src.text_summarizer.custom_exception import CustomExeption
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import sys

@ensure_annotations
def read_yaml(path_to_yaml:Path) -> ConfigBox:
    '''
    Read yaml file and returns
    
    Args:
        path to yaml file
    
    Raises:
        Custom exception

    Returns:
        ConfigBox- Config Box Type
        
    '''

    try:
        with open(path_to_yaml, 'r') as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f'yaml file: {yaml_file} loaded successfully')
            return ConfigBox(content)
        
    except Exception as e:
        raise CustomExeption(e,sys)

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    
    '''
    create list of directories

    Args:
        path_to_directories list - list of path directories
        ignore_log (bool, optional) - ignore if multiple directories to be created, defalut to false
    '''
    
    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f'Created directory at : {path}')


@ensure_annotations
def get_size(path:Path) -> str:

    '''
    get size of file in KB

    Agrs:
        path(Path) : Path of File

    Returns:
        str: size in KB        
    '''
    size_in_kb = round(os.path.getsize(path)/1024)
    return f'~ {size_in_kb} KB'

