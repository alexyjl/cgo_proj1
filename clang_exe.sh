#testpath=$HOME/study/cgo/testing
clang -cc1 -load ../../../../Release+Asserts/lib/libConstructCFG.so -plugin construct-cfg $1.c 2>$1.dot_&&
python process.py $1.dot_ $1.dot &&
dot -Tgif $1.dot -o $1.gif


