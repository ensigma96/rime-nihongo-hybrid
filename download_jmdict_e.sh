#!/bin/bash

readonly JMDICT_E_URI='ftp://ftp.monash.edu.au/pub/nihongo/JMdict_e.gz'
readonly DIR=`pwd`
readonly JMDICT_DIR="${DIR}/src/data/JMdict"
readonly JMDICT_E="${JMDICT_DIR}/JMdict_e.xml"

wget -O - "${JMDICT_E_URI}" | gzip -d > "${JMDICT_E}"
