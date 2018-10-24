import unittest, lossfiles

class ModelClassInputs(unittest.TestCase):
    def test_model_code_accepts_int_only(self):
        l = lossfiles.file_meta_data(5,0000,'stc'); self.assertTrue(type(l.model) is int)
        l = lossfiles.file_meta_data('5',0000,'stc'); self.assertFalse(type(l.model) is int)
        l = lossfiles.file_meta_data(5.0,0000,'stc'); self.assertFalse(type(l.model) is int)

class FileTypeClassInputs(unittest.TestCase):
    def test_inx_accepts_only_one_of_two_types(self):
        x = lossfiles.inx(5,0000,'stc','not_rect_or_jagged')
        self.assertFalse(x.file_shape in ['rect','jagged'])


if __name__ == "__main__":
    unittest.main()