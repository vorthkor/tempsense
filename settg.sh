#!/bin/bash

touch $HOME/tempsense/docs/temp.txt
touch $HOME/tempsense/docs/hour.txt
sudo chmod -R 777 $HOME/tempsense

mv $HOME/tempsense/scripts/*.sh $HOME
mv $HOME/tempsense/scripts/tempsense.service $HOME