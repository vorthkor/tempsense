#!/bin/bash

sudo chmod -R 777 $HOME/tempsense

touch $HOME/tempsense/docs/temp.txt
touch $HOME/tempsense/docs/hour.txt
touch $HOME/tempsense/docs/last.txt
touch $HOME/tempsense/docs/logh.txt

cp -R $HOME/tempsense/scripts/*.sh $HOME
cp $HOME/tempsense/scripts/tempsense.service $HOME