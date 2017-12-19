#!/bin/bash

readonly INTERNET_JP_FORMS_URI='http://corpus.leeds.ac.uk/frqc/internet-jp-forms.num'
readonly DIR=`pwd`
readonly INTERNET_JP_FORMS="${DIR}/src/data/internet-jp-forms.num"

wget -O - "${INTERNET_JP_FORMS_URI}" > ${INTERNET_JP_FORMS}
