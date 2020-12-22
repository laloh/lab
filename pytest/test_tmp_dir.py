​def​ test_tmpdir_factory(tmpdir_factory):
    ​# you should start with making a directory​
    ​# a_dir acts like the object returned from the tmpdir fixture​ a_dir = tmpdir_factory.mktemp(​'mydir'​)
    ​# base_temp will be the parent dir of 'mydir'​ ​# you don't have to use getbasetemp()​
    ​# using it here just to show that it's available​ base_temp = tmpdir_factory.getbasetemp() ​print​(​'base:'​, base_temp)
    ​# the rest of this test looks the same as the 'test_tmpdir()'​ ​# example except I'm using a_dir instead of tmpdir​
    a_file = a_dir.join(​'something.txt'​)
    a_sub_dir = a_dir.mkdir(​'anything'​)
    another_file = a_sub_dir.join(​'something_else.txt'​)
    a_file.write(​'contents may settle during shipping'​) another_file.write(​'something different'​)
    ​assert​ a_file.read() == ​'contents may settle during shipping'​ ​assert​ another_file.read() == ​'something different'