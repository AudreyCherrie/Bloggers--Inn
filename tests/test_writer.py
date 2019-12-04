import unittest
from app.models import Writer

'''
we test to see if our password is being hashed
'''
class WriterModelTest(unittest.TestCase):
    def setUp(self):
        self.new_writer=Writer(password='car')
        '''
        we then need to confirm that after the password is hashed the variable containsa value
        '''
    def test_password_hasher(self):
        self.assertTrue(self.new_writer .pass_secure is not None)

    def no_access(self):
        with self.assertRaises(AttributeError):
            self.new_writer.password
            '''
            we  test to see our hashed password can be confirmed
            '''

    def test_verification(self):
        self.assertTrue(self.new_writer.verify_password('car'))
