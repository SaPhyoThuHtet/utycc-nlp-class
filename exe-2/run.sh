python to-crf-format-PhyoThuHtet.py test.data > test.data.formated

# Getting Result From CRF Model
crf_test -m model test.data.formated > test.result


# PostProcessing of crf resulted file
python postprocessing-PhyoThuHtet.py test.result > result-by-crf


# Check Word Segmenatation
python word-seg-check-PhyoThuHtet.py test.data result-by-crf > checked.txt
gedit checked.txt

