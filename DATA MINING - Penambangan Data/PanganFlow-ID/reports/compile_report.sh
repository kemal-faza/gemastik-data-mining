#!/bin/bash
# compile_report.sh -- Compile LaTeX report to PDF
cd "$(dirname "$0")"
echo "Compiling panganflow_report.tex..."
pdflatex -interaction=nonstopmode panganflow_report.tex > /dev/null 2>&1
pdflatex -interaction=nonstopmode panganflow_report.tex > /dev/null 2>&1
if [ -f panganflow_report.pdf ]; then
    filesize=$(ls -lh panganflow_report.pdf | awk '{print $5}')
    echo "OK: panganflow_report.pdf ($filesize)"
else
    echo "ERROR: PDF not generated. Check panganflow_report.log"
    exit 1
fi
