import os
import sys
import re


def from_dict(dct):
    def lookup(match):
        key = match.group(1)
        return dct.get(key, f'<{key} not found>')
    return lookup


def clean_template(test_counter):
    file_name = "test_cases/qa"+str(test_counter)+"_tx_rx.py"
    f = open(
        file_name, 'w')
    f.close()


def write_template(test_counter, source_data, bw, sf, paylen, impl_head, has_crc, cr):
    file_name = "test_cases/qa"+str(test_counter)+"_tx_rx.py"
    f_template = open(
        'template/testcase_tx_rx.py', 'r')
    f_template_text = f_template.read()
    subs = {
        "filename": str(test_counter),
        "source_data": str(source_data),
        "bw": str(bw),
        "sf": str(sf),
        "pay_len": str(paylen),
        "impl_head": str(impl_head),
        "has_crc": str(has_crc),
        "cr": str(cr)
    }
    replaced_text = re.sub('@@(.*?)@@', from_dict(subs), f_template_text)

    f = open(file_name, "a")
    f.write(replaced_text)
    f.close()


def write_cmake_begin():
    file_name = "CMakeList.txt"
    f = open(file_name, "w")
    f.close()


def update_cmake(test_counter):
    file_name = "CMakeList.txt"
    f = open(file_name, "a")
    subs = {
        "test_counter": str(test_counter),
    }
    str_add = "GR_ADD_TEST(qa@@test_counter@@_tx_rx ${PYTHON_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/qa@@test_counter@@_tx_rx.py) \n"
    replaced_text = re.sub('@@(.*?)@@', from_dict(subs), str_add)
    f.write(replaced_text)
    f.close()
