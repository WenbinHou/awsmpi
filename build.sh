
cd "$(dirname "$(realpath ""$0)")"

rm dist/*

python setup.py bdist_wheel

twine upload dist/*

