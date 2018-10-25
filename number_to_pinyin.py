# coding=utf-8 # add this to solve unicode issue
# written by @Tester2009
# October 26, 2018
# show error name and file, and line where it go wrong: https://stackoverflow.com/a/1278740
# solve issue unicode which is > " SyntaxError: Non-ASCII character '\xc3' in file number_to_pinyin.py on line 40, but no encoding declared; see http://python.org/dev/peps/pep-0263/ for details " by using this solution: https://stackoverflow.com/a/26899264
# split integer or string into array: https://stackoverflow.com/a/1906723
# source for spelling: https://blogs.transparent.com/chinese/chinese-numbers-1-100/
import sys, os

def main():
    number_to_pinyin()

def number_to_pinyin():
    # check length of input
    try:
        REQUEST_INPUT = int(abs(input('Input your number: '))) # abs is to get absolute value of number. will convert negative number (if exist) to positive: https://www.codevscolor.com/count-number-digits-number-python/
        # print(REQUEST_INPUT)
        # check for length of input
        CHANGE_INT_TO_STR_RQ_INPUT = str(REQUEST_INPUT)
        LENGTH_OF_INPUT = len(CHANGE_INT_TO_STR_RQ_INPUT)
        # print(str(LENGTH_OF_INPUT))
        if LENGTH_OF_INPUT==1:
            # basically from 0 to 9
            print('0 - 9')
            print(REQUEST_INPUT)
            print( pinyin_first(REQUEST_INPUT) )
        if LENGTH_OF_INPUT==2:
            # basically from 10 to 99
            print('10 - 99')
            # have to check first integer and 2nd integer
            SPLICE_INTEGER_ = list(str(REQUEST_INPUT))
            if int(SPLICE_INTEGER_[1])==0:
                # if the 2nd integer is zero, don't need to add "Líng"
                print( ten_number(SPLICE_INTEGER_[0]) )
            else:
                print( ten_number(SPLICE_INTEGER_[0]) + " " + pinyin_first(SPLICE_INTEGER_[1]) )
        if LENGTH_OF_INPUT==3:
            # basically from 100 to 999
            print('100 to 999')
            SPLICE_INTEGER_ = list(str(REQUEST_INPUT))
            # print(SPLICE_INTEGER_)
            # identify each number please
            # if int(SPLICE_INTEGER_[1])==0 and int(SPLICE_INTEGER_[2])!=0:
            #     # tell how to pronounce it properly
            #     print( pinyin_first(SPLICE_INTEGER_[0]) + " Bǎi Ling " + pinyin_first(SPLICE_INTEGER_[2]) ) # add "Bǎi Ling"
            #
            # #
            # if int(SPLICE_INTEGER_[1])!=0 and int(SPLICE_INTEGER_[2])!=0:
            #     print( pinyin_first(SPLICE_INTEGER_[0]) + " Bǎi " + ten_number(SPLICE_INTEGER_[1]) + " " + pinyin_first(SPLICE_INTEGER_[2]) ) # add "Bǎi Ling"
            #
            #
            # if int(SPLICE_INTEGER_[1])==0 and int(SPLICE_INTEGER_[2])==0:
            #     # now only pronounce without "Líng"
            #     print( pinyin_first(SPLICE_INTEGER_[0]) + " Bǎi ") # add "Bǎi Ling"



    except Exception as e_message:
        GET_ERROR_INFO = throwError('errName')
        # print(GET_ERROR_INFO)
        if GET_ERROR_INFO=="SyntaxError":
            print("Please input integer only! 1")
        if GET_ERROR_INFO=="NameError":
            print("Please input integer only! 2")

def hundred_number(VAL):
    CHG_VAL_INT_ = int(VAL)
    print(CHG_VAL_INT_)


def ten_number(VAL):
    CHG_VAL_INT_ = int(VAL)
    if CHG_VAL_INT_ == 1:
        return "Shí" # this is unique
    RTN_VAL_TEN_NMBR = pinyin_first(CHG_VAL_INT_)+" shí"
    return RTN_VAL_TEN_NMBR

def pinyin_first(VAL):
    CHG_VAL_INT_ = int(VAL)
    if CHG_VAL_INT_==0:
        return "Líng"
    if CHG_VAL_INT_==1:
        return "Yī"
    if CHG_VAL_INT_==2:
        return "Èr"
    if CHG_VAL_INT_==3:
        return "Sān"
    if CHG_VAL_INT_==4:
        return "Sì"
    if CHG_VAL_INT_==5:
        return "Wǔ"
    if CHG_VAL_INT_==6:
        return "Liù"
    if CHG_VAL_INT_==7:
        return "Qī"
    if CHG_VAL_INT_==8:
        return "Bā"
    if CHG_VAL_INT_==9:
        return "Jiǔ"

def throwError(TYPE_OF_ERROR_):
    # written by @Tester2009
    # October 26, 2018
    EXCEPTION_TYPE, exc_obj, exc_tb = sys.exc_info()
    FILENAME_OF_ERROR_FILE = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    if str(TYPE_OF_ERROR_)=="all":
        # print(exc_type, fname, exc_tb.tb_lineno)
        # print("Exception name: "+str(exc_type)+"\nFile name: "+str(fname)+"\nError in line: "+str(exc_tb.tb_lineno))
        RETURN_ERROR_VALUE_ = "Exception name: "+str(EXCEPTION_TYPE)+"\nFile name: "+str(FILENAME_OF_ERROR_FILE)+"\nError in line: "+str(exc_tb.tb_lineno)
    if str(TYPE_OF_ERROR_)=="errName":
        ERROR_NAME = str(EXCEPTION_TYPE)
        # print(ERROR_NAME.split()[1][1:-2].split('.')[1]) # full code
        GET_EXCEPTION_NAME = ERROR_NAME.split()[1] # split between type and exception name. get the exception name
        CLEAN_EXCEPTION_NAME = GET_EXCEPTION_NAME[1:-2] # now to remove apostrophe from front and back. also to remove > from back
        SPLIT_EXCEPTION_NAME = CLEAN_EXCEPTION_NAME.split('.') # now to split between exception string and exception name string. split by using dot.
        EXCEPTION_NAME_RESULT = SPLIT_EXCEPTION_NAME[1] # now access it
        RETURN_ERROR_VALUE_ = EXCEPTION_NAME_RESULT
    else:
        print("nope")
    return RETURN_ERROR_VALUE_

if __name__ == "__main__":
    main()
