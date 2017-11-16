#!/bin/bash

readonly DIR=`pwd`
readonly SRC="${DIR}/src"
readonly STUB="${SRC}/stub"
readonly DATA="${SRC}/data"
readonly CONVERTER="${SRC}/converter"
readonly MOZC_DICT_DIR="${DATA}/mozc_dictionaries"
readonly DIST="${DIR}/dist"

rm -rf "${DIST}"
mkdir -p "${DIST}"
cp -r "${STUB}/." "${DIST}"
python3 "${CONVERTER}/main.py" ${MOZC_DICT_DIR} >> "${DIST}/nihongo-hybrid.dict/nihongo-hybrid.mozc.dict.yaml"
