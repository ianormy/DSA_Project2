"""
Active Directory

For this problem, the goal is to write code for finding all files under a directory (and all directories beneath it)
that end with ".c"
"""
import unittest
from tempfile import TemporaryDirectory as TempDir
import os


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    if suffix is None or len(suffix) == 0:
        raise ValueError("suffix cannot be None or empty")
    if not os.path.isdir(path):
        raise ValueError("input path is not a directory: {}".format(path))
    paths = []
    files = os.listdir(path)
    for file in files:
        full_path = os.path.join(path, file)
        if os.path.isfile(full_path):
            if file.endswith(suffix):
                paths.append(full_path)
        if os.path.isdir(full_path):
            ret = find_files(suffix, full_path)
            if ret:
                paths.append(ret)
    return paths if len(paths) > 0 else None


class FindFilesTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.directory = TempDir()
        with open(os.path.join(cls.directory.name, 'test.h'), 'w') as f:
            f.write("/* test.h */\n")
        os.mkdir(os.path.join(cls.directory.name, "sub"))
        temp_file_name = os.path.join(os.path.join(cls.directory.name, "sub"), 'test.c')
        with open(temp_file_name, 'w') as f:
            f.write("/* test.c */\n")

    def test_valid_search(self):
        ret = find_files(suffix=".c", path=self.directory.name)
        self.assertEqual(len(ret), 1)
        print(ret)

    def test_invalid_path(self):
        with self.assertRaises(ValueError):
            find_files(suffix=".dat", path="!invalid path!")

    def test_missing_suffix(self):
        with self.assertRaises(ValueError):
            find_files(suffix='', path=self.directory.name)


if __name__ == '__main__':
    unittest.main()
