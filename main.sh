#!/bin/bash

readonly DIR=`pwd`
readonly SRC="${DIR}/src"
readonly STUB="${SRC}/stub"
readonly DICT="${STUB}/dict"
readonly SCHEMA="${STUB}/schema"
readonly OPENCC="${STUB}/opencc"
readonly DATA="${SRC}/data"
readonly OPENCC_DATA="${DATA}/opencc"
readonly MOZC_DICT_DIR="${DATA}/mozc_dictionaries"
readonly CONVERTER="${SRC}/converter"
readonly DIST="${DIR}/dist"

rm -rf "${DIST}"
mkdir -p "${DIST}"
cp -r "${DICT}/." "${DIST}"
cp -r "${OPENCC}" "${DIST}"
cp -r "${OPENCC_DATA}" "${DIST}"
cp "${SCHEMA}/nihongo-hybrid.schema.yaml" "${DIST}"
python3 "${CONVERTER}/mozc.py" ${MOZC_DICT_DIR} >> "${DIST}/nihongo-hybrid.dict/nihongo-hybrid.mozc.dict.yaml"
python3 "${CONVERTER}/kana.py" >> "${DIST}/nihongo-hybrid.dict/nihongo-hybrid.kana.dict.yaml"
