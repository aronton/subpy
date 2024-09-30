#!/bin/bash
#SBATCH --partition=replace1
#SBATCH --ntasks=1
#SBATCH --job-name=replace2
#SBATCH --cpus-per-task=replace3
#SBATCH --output=replace4

date

Spin=${1}

tSDRG_path=${12}

output_path=${13}

echo -e "current dir:"
cd $tSDRG_path"/tSDRG/Main_"$Spin

pwd

# echo "script_directory"
# echo "$output_path"

L=${2}

J=${3}

D=${4}

BC=${5}

bonDim=${6}

Pdis=${7}

s1=${8}

s2=${9}

CheckOrNot=${10}

Ncore=${11}

echo "Spin         ==> $Spin"
echo "L         ==> $L"
echo "J         ==> $J"
echo "D         ==> $D"
echo "BC        ==> $BC"
echo "bonDim        ==> $bonDim"
echo "Pdis        ==> $Pdis"
echo "s1        ==> $s1"
echo "s2        ==> $s2"
echo "CheckOrNot        ==> $CheckOrNot"
echo "Ncore        ==> $Ncore"
echo "tSDRG_path        ==> $tSDRG_path"
echo "output_path        ==> $output_path"

$tSDRG_path/tSDRG/Main_${Spin}/Spin${Spin}_gaussian.exe $L $bonDim $Pdis $J $D $BC $s1 $s2 $CheckOrNot
echo "tSDRG_path/tSDRG/Main/Spin${Spin}_gaussian.exe $L $bonDim $Pdis $J $D $BC $s1 $s2 $CheckOrNot"

date
