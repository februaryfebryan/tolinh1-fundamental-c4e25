import pyexcel
from collections import OrderedDict #để cho dictionary được sắp xếp đúng trật tự trong excel


random_dictionary = [
    OrderedDict({
        "chu dau tien" : 'a',
        "chu thu hai" : 'b',
        "chu thu ba" : 'c'
    }),

    OrderedDict({
        "chu dau tien": '1',
        "chu thu hai": '2',

    }),
]
   
pyexcel.save_as(records = random_dictionary, dest_file_name = "bla1.xls")