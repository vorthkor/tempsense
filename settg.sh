#!/bin/bash

sudo chmod -R 777 $HOME/tempsense

touch $HOME/tempsense/docs/temp.txt
touch $HOME/tempsense/docs/hour.txt
touch $HOME/tempsense/docs/last.txt
touch $HOME/tempsense/docs/logh.txt

mv $HOME/tempsense/scripts/*.sh $HOME
mv $HOME/tempsense/scripts/tempsense.service $HOME