# find out where is your python
# Windows : where python

which python
>>/usr/bin/python

# into folder
cd /usr/bin

# list the folder
ls -al

# find out "symbolic link"(符號鏈接)
# ex1.python -> python2 
# ex2.python2 -> python2.7
# ex3.python3 -> python3.7


# check version
python --version


# change path
# ln:修改符號鏈接
# -s:soft 軟鏈接
# -f:force:強制覆蓋現有鏈接
# 讓python指向python3.7
sudo ln -sf python3 python

# check version
python --version

