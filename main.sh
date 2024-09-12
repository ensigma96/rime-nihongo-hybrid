#!/bin/bash

readonly DIR=`pwd`

readonly SRC="${DIR}/src"
readonly STUB="${DIR}/stub"

readonly DATA="${DIR}/data"
readonly OPENCC_JPVARIANTS_TEXT="${DATA}/opencc/JPVariants.txt"
readonly MOZC_DICT_DIR="${DATA}/mozc_dictionaries"
readonly JMDICT_E="${DATA}/JMdict/JMdict_e.xml"

readonly DIST="${DIR}/dist"

rm -rf "${DIST}"
mkdir -p "${DIST}"
cp -r "${STUB}/." "${DIST}/"
opencc_dict -i "${OPENCC_JPVARIANTS_TEXT}" -o "${DIST}/opencc/JPVariants.ocd" -f text -t ocd
python3 "${SRC}/mozc.py" "${MOZC_DICT_DIR}" >> "${DIST}/nihongo-hybrid.dict/nihongo-hybrid.mozc.dict.yaml"
python3 "${SRC}/jmdict.py" "${JMDICT_E}" >> "${DIST}/nihongo-hybrid.dict/nihongo-hybrid.jmdict.dict.yaml"
python3 "${SRC}/kana.py" >> "${DIST}/nihongo-hybrid.dict/nihongo-hybrid.kana.dict.yaml"
