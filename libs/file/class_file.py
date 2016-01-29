# coding=UTF-8

# --------------------------------------------------------------
# class_File文件
# @class: File
# @introduction: File类用来处理文件
# @dependency: os, os.path包
# @author: plutoese
# @date: 2016.01.28
# --------------------------------------------------------------

import os
import re
import datetime


class File:
    """File类用来处理文件

    """
    def __init__(self, file_name_with_dir):
        if os.path.isfile(file_name_with_dir):
            self.__file_name_with_dir = file_name_with_dir
        else:
            print('{} is not a directory!'.format(file_name_with_dir))
            raise FileNotFoundError

        self.__dir, self.__full_file_name = os.path.split(self.__file_name_with_dir)
        self.__file_name, self.__file_extension = re.split('\.',self.__full_file_name)
        # 处理分解文件名
        self.__filename_parse()

    @property
    def last_modified(self):
        return datetime.datetime.fromtimestamp(os.path.getmtime(self.__file_name_with_dir))

    @property
    def file_name(self):
        return self.__full_file_name

    @property
    def directory(self):
        return self.__dir

    @property
    def extension(self):
        return self.__file_extension

    @property
    def author(self):
        return self.__author

    @property
    def time(self):
        return self.__time

    @property
    def version(self):
        return self.__version

    @property
    def tags(self):
        return self.__tags

    @property
    def dirs(self):
        return self.__dirs

    @property
    def new_file_name(self):
        return self.__new_file_name

    def __len__(self):
        return os.path.getsize(self.__file_name_with_dir)

    def same_file(self, file_name):
        return os.path.samefile(self.__file_name_with_dir,file_name)

    def __filename_parse(self):
        """辅助函数，分解文件名：作者，时间，版本，标签，目录

        :return: 无返回值
        """
        self.__new_file_name = re.split('[@#%$&]',self.__file_name,maxsplit=1)[0]
        self.__author = None
        self.__time = None
        self.__version = None
        self.__tags = None
        self.__dirs = None

        # 析出作者
        tmp_search_result = re.search('@[a-zA-Z0-9]+',self.__file_name)
        if tmp_search_result is not None:
            self.__author = re.sub('@','',tmp_search_result.group())

        # 析出时间
        tmp_search_result = re.search('#[a-zA-Z0-9]+',self.__file_name)
        if tmp_search_result is not None:
            self.__time = re.sub('#','',tmp_search_result.group())

        # 析出版本号
        tmp_search_result = re.search('$[a-zA-Z0-9]+',self.__file_name)
        if tmp_search_result is not None:
            self.__version = re.sub('$','',tmp_search_result.group())

        # 析出标签
        tmp_search_result = re.search('%[a-zA-Z0-9%]+',self.__file_name)
        if tmp_search_result is not None:
            self.__tags = [item for item in re.split('%',tmp_search_result.group()) if len(item) > 0]

        # 析出目录
        tmp_search_result = re.search('&[a-zA-Z0-9&]+',self.__file_name)
        if tmp_search_result is not None:
            self.__dirs = [item for item in re.split('&',tmp_search_result.group()) if len(item) > 0]


if __name__ == '__main__':
    file = File('D:/down/demo@glen#2012%database%mongodb.xlsx')
    print(file.file_name)
    print(file.directory)
    print(file.extension)
    print(file.last_modified)
    print(len(file))
    print(file.same_file('D:/down/demo@glen#2012%database%mongodb.xlsx'))
    print(file.author)
    print(file.dirs)
    print(file.time)
    print(file.version)
    print(file.tags)
    print(file.dirs)
    print(file.new_file_name)