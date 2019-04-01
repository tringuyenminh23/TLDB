import filecmp

from config import root_path
from test.tests import TestCaseCompare
from tldb.core.tldb import TLDB


class TestTLDB(TestCaseCompare):
    @classmethod
    def setUpClass(cls):
        super(TestTLDB, cls).setUpClass()
        cls.tldb = TLDB('local')
        cls.input_folder = root_path() / 'test' / 'io' / 'in' / 'cases' / 'simple_small'
        cls.output_folder = cls.output_folder / 'core' / 'tldb'

    def test_rtree_index_csv_file(self):
        method_id = self.id().split('.')[-1]
        self.prepare_compare_files(method_id)

        self.tldb.load_object_from_csv('table', self.input_folder / 'A_B_D_table.dat', delimiter=' ', index_type='rtree',
                                       headers=['A', 'B', 'D'])

        with self.out_file[method_id].open(mode='w') as f:
            f.write(str(self.tldb.objects['table']))

        self.file_compare(self.out_file[method_id], self.exp_file[method_id])

    def test_rtree_index_xml_file(self):
        method_id = self.id().split('.')[-1]
        self.prepare_compare_files(method_id)

        self.tldb.load_object_from_xml('xml', root_path() / 'test' / 'io' / 'in' / 'lib' / 'messages.xml')
        with self.out_file[method_id].open(mode='w') as f:
            f.write(str(self.tldb.objects['xml']))
        self.file_compare(self.out_file[method_id], self.exp_file[method_id])

    def test_rtree_index_from_folder(self):
        method_id = self.id().split('.')[-1]
        self.prepare_compare_files(method_id)

        tldb = TLDB('simple_small')
        tldb.load_from_folder(self.input_folder)
        with self.out_file[method_id].open(mode='w') as f:
            for obj in tldb.objects:
                f.write(str(tldb.objects[obj]))
                f.write('-' * 20 + '\n')
        self.file_compare(self.out_file[method_id], self.exp_file[method_id])

