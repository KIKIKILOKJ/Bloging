import unittest
from app.models import Post, User


class PostTest(unittest.TestCase):
    '''
    Test class to test the behaviour of the Post class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_post = Post("hello","We are the posts","kimonyoski")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_post,Post))

class UserModelTest(unittest.TestCase):
    def setUp(self):
        self.new_user = User(password_hash= 'banana')
        
    def test_password_setter(self):
        self.assertTrue(self.new_user.password_hash is not None)
        
    def test_no_access_password(self):
        with self.assertRaises(AttributeError):
            self.new_user.password
            
    def test_password_verification(self):
        self.assertTrue(self.new_user.verify_password('banana'))
