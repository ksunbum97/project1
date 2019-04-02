#!/bin/bash
declare -a words

while true
do
        read -p "Enter a new word: " word
        if [ $word = "list" ]; then
                echo ${words[*]}
                continue
        elif [ $word = "quit" ]; then
                exit 0
        else
                words+=($word)
                echo "Length: ${#words[@]}"
                continue
        fi
done

