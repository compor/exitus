#!/usr/bin/env bash

[[ -z $1 ]] && echo "missing input file" && exit 1

CUR_DIR=$(cd $(dirname ${BASH_SOURCE[0]}) && pwd)

DOT_PREFIX=${1%.dot}

TMP_ORDER_FILE=${DOT_PREFIX}".order"
TMP_DOT_FILE1=${DOT_PREFIX}".tmp1.dot"
TMP_DOT_FILE2=${DOT_PREFIX}".tmp2.dot"

DOT_OUTPUT=${DOT_PREFIX}".colorized.dot"
PDF_OUTPUT=${DOT_PREFIX}".colorized.pdf"

trap "rm -rf ${TMP_DOT_FILE1} ${TMP_DOT_FILE2} ${TMP_ORDER_FILE}" EXIT

${CUR_DIR}/lib/gv-dot-get-order.sh ${1} ${TMP_ORDER_FILE} && \
${CUR_DIR}/lib/gv-dot-colorize.py ${1} ${TMP_DOT_FILE1} && \
${CUR_DIR}/lib/gv-dot-node-linearize.sh ${TMP_DOT_FILE1} > ${TMP_DOT_FILE2} && \
${CUR_DIR}/lib/gv-dot-sort-precomputed-order.sh ${TMP_DOT_FILE2} ${TMP_ORDER_FILE} ${DOT_OUTPUT} && \
dot -Tpdf ${DOT_OUTPUT} -o ${PDF_OUTPUT}

exit $?

