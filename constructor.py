import EXWriting
#import md_writer
import test1
import number_charact

def character_creater():
    vn_result = []
    #test1.test_An(vn_result)
    vn_result = test1.test_An()

    number_charact.number_charactristic(vn_result)
    EXWriting.Excel_file_writing(vn_result)
    #md_writer.text_md(vn_result)