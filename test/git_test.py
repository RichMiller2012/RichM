from git_utils import *
from tests.plugins.ReqTracer import requirements
from unittest import TestCase
from mock import Mock
from mock import patch
import os

class GitTest(TestCase):


    def test_is_file_path_in_repo_no(self):
        os.path.exists = Mock(return_value=False)
        self.assertEqual(is_file_in_repo('path'),'No')


    @requirements(['#0100'])
    @patch('git_utils.get_diff_files', return_value=['other_path'])
    @patch('git_utils.get_untracked_files', return_value=['other_path'])
    def test_is_file_abs_path_in_repo_yes(self, path, other):
        os.path.exists = Mock(return_value=True)
        os.path.isabs = Mock(return_value=False)
        self.assertEqual(is_file_in_repo('path'), 'Yes')

    @requirements(['#0110'])
    @patch('git_utils.get_diff_files', return_value=['path'])
    def test_is_file_other_files(self, get_diff_files):
        os.path.exists = Mock(return_value=True)
        os.path.isabs = Mock(return_value=True)
        result = is_file_in_repo('path')
        self.assertEqual(result, 'No')

    @requirements(['#0101'])
    @patch('git_utils.get_diff_files', return_value=['path'])
    def test_modified_locally(self, get_diff_files):
        os.path.exists = Mock(return_value=True)
        os.path.isabs = Mock(return_value=False)
        os.path.abspath = Mock(return_value='path')
        result = get_git_file_info('path')
        self.assertEqual(result, "path has been modified locally")

    @requirements(['#0111'])
    @patch('git_utils.get_diff_files', return_value=['other_path'])
    @patch('git_utils.get_untracked_files', return_value=['path'])
    def test_not_checked_in(self, other_path, path):
        os.path.exists = Mock(return_value=True)
        os.path.isabs = Mock(return_value=False)
        os.path.abspath = Mock(return_value='path')
        result = get_git_file_info('path')
        self.assertEqual(result, 'path has been not been checked in')

    @requirements(['#0121'])
    @patch('git_utils.get_diff_files', return_value=['other_path'])
    @patch('git_utils.get_untracked_files', return_value=['other_path'])
    @patch('git_utils.is_repo_dirty', return_value=True)
    def test_is_dirty_repo(self, diff_path, other_path, dirty):
        os.path.exists = Mock(return_value=True)
        os.path.isabs = Mock(return_value=False)
        os.path.abspath = Mock(return_value='path')
        result = get_git_file_info('path')
        self.assertEqual(result, 'path is a dirty repo')

    @requirements(['#0131'])
    @patch('git_utils.get_diff_files', return_value=['other_path'])
    @patch('git_utils.get_untracked_files', return_value=['other_path'])
    @patch('git_utils.is_repo_dirty', return_value=False)
    def test_is_up_to_date(self, diff_path, other_path, dirty):
        os.path.exists = Mock(return_value=True)
        os.path.isabs = Mock(return_value=False)
        os.path.abspath = Mock(return_value='path')
        result = get_git_file_info('path')
        self.assertEqual(result, 'path is up to date')


    @requirements(['#0141'])
    @patch('git_utils.has_diff_files', return_value=True)
    @patch('git_utils.has_untracked_files', return_value=False)
    def test_func_is_repo_dirty(self, has_diff_files, untracked):
        os.path.exists = Mock(return_value=True)
        self.assertTrue(is_repo_dirty('path'))


    @requirements(['#0151'])
    @patch('git_utils.has_diff_files', return_value=False)
    @patch('git_utils.has_untracked_files', return_value=False)
    def test_func_is_repo_not_dirty(self, has_diff_files, untracked):
        os.path.exists = Mock(return_value=True)
        self.assertFalse(is_repo_dirty('path'))

    @requirements(['#0161'])
    @patch('git_utils.get_diff_files', return_value='path')
    def test_func_has_diff_files(self, diff):
        os.path.exists = Mock(return_value=True)
        self.assertTrue(has_diff_files('path'))

    @requirements(['#0171'])
    @patch('git_utils.get_diff_files', return_value='')
    def test_func_has_diff_no_files(self, diff):
        os.path.exists = Mock(return_value=True)
        self.assertFalse(has_diff_files('path'))

    @requirements(['#0181'])
    @patch('git_utils.get_untracked_files', return_value='path')
    def test_func_has_untracked_files(self, untracked):
        os.path.exists = Mock(return_value=True)
        self.assertTrue(has_untracked_files('path'))

    @requirements(['#0191'])
    @patch('git_utils.get_untracked_files', return_value='')
    def test_func_has_untracked_no_files(self, untracked):
        os.path.exists = Mock(return_value=True)
        self.assertFalse(has_untracked_files('path'))

    @requirements(['#0102'])
    @patch('git_utils.git_execute', return_value='<hash>, <date modified>, <author>')
    def test_func_get_file_info(self, execute):
        os.path.exists = Mock(return_value=True)
        self.assertEqual(get_file_info('path'), '<hash>, <date modified>, <author>')

    @requirements(['#0112'])
    @patch('git_utils.git_execute', return_value='file1\nfile2')
    @patch('git_utils.get_repo_root', return_value='root')
    def test_func_get_diff_files(self, execute, root):
        os.path.exists = Mock(return_value=True)
        result = get_diff_files('path')
        self.assertEqual(result, ['root\\file1','root\\file2','root\\file1','root\\file2'])

    @requirements(['#0113'])
    @patch('git_utils.git_execute', return_value='file1\nfile2')
    @patch('git_utils.get_repo_root', return_value='root')
    def test_func_get_untracked_files(self, execute, root):
        os.path.exists = Mock(return_value=True)
        result = get_untracked_files('path')
        self.assertEqual(result,['root\\file1','root\\file2'])

    @requirements(['#0113'])
    @patch('git_utils.git_execute', return_value='\\folder\\file')
    def test_func_get_repo_root(self, execute):
        os.path.exists = Mock(return_value=True)
        os.path.isfile = Mock(return_value=True)
        os.path.dirname = Mock(return_value='path')
        result = get_repo_root('path')
        self.assertEqual(result, '\\folder\\file')

    @requirements(['#0103'])
    @patch('git_utils.git_execute', return_value='branch')
    def test_func_get_repo_branch(self, execute):
        os.path.exists = Mock(return_value=True)
        os.path.isfile = Mock(return_value=True)
        os.path.dirname = Mock(return_value='path')
        self.assertEqual(get_repo_branch('path'), 'branch')


    @requirements(['#0104'])
    @patch('git_utils.git_execute', return_value='url')
    def test_func_get_repo_url(self, execute):
        os.path.exists = Mock(return_value=True)
        os.path.isfile = Mock(return_value=True)
        os.path.dirname = Mock(return_value='path')
        self.assertEqual(get_repo_url('path'), 'url')

    def test_func_execute_git(self):
        result = git_execute(['git', 'config', '--get', 'remote.origin.url'])
        self.assertTrue(isinstance(result, str))





   # @requirements(['#0101'])
  #  @requirements(['#0102'])
  #  @requirements(['#0103'])
 #   @requirements(['#0104'])


