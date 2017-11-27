#!/bin/bash

source './main.conf'

readonly DIR=`pwd`
readonly SRC="${DIR}/src"
readonly STUB="${SRC}/stub"
readonly DICT="${STUB}/dict"
readonly SCHEMA="${STUB}/schema"
readonly OPENCC="${STUB}/opencc"
readonly DATA="${SRC}/data"
readonly CONVERTER="${SRC}/converter"
readonly MOZC_DICT_DIR="${DATA}/mozc_dictionaries"
readonly DIST="${DIR}/dist"

rm -rf "${DIST}"
mkdir -p "${DIST}"
cp -r "${DICT}/." "${DIST}"
if [[ "${OPENCC_LEGACY_MODE}" -eq $zero ]]; then
	cp -r "${OPENCC}" "${DIST}"
	cp "${SCHEMA}/nihongo-hybrid.schema.yaml" "${DIST}"
else
	cp "${SCHEMA}/nihongo-hybrid.legacy.schema.yaml" "${DIST}/nihongo-hybrid.schema.yaml"
fi
python3 "${CONVERTER}/main.py" ${MOZC_DICT_DIR} >> "${DIST}/nihongo-hybrid.dict/nihongo-hybrid.mozc.dict.yaml"
