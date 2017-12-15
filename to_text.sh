#!/bin/bash
outputDir=$1

echo $outputDir

if [ -n $outputDir ]
then
  for file in *
  do
    len=${#file}
    let 'len -= 4'
    output="${file:0:len}.txt"
    pdf2txt.py "$file" > "$outputDir/$output"
  done
else
  echo "Use command in the format to_text.sh [inputDir] [outputDir]"
fi
