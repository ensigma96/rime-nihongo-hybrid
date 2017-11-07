#!/bin/bash

readonly DIR=`pwd`
readonly SRC="${DIR}/src"
readonly MOZC_DICT_DIR="${SRC}/mozc_dictionaries"
readonly DIST="${DIR}/dist"

rm -rf "${DIST}"
mkdir -p "${DIST}"
cp ${SRC}/nihongo-hybrid.schema.yaml "${DIST}/"
cp ${SRC}/nihongo-hybrid.dict.yaml "${DIST}/"
cp -r ${SRC}/nihongo-hybrid.dict "${DIST}/"
python3 main.py ${MOZC_DICT_DIR} >> ${DIST}/nihongo-hybrid.dict/nihongo-hybrid.mozc.dict.yaml
