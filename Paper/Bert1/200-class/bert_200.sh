#!/bin/bash
#SBATCH --job-name=200_bert1
#SBATCH --time=6:00:00
#SBATCH --mem=80GB
#SBATCH --error=/home/limei/ProtoryNet/Paper/Bert1/200-class/200_s1.err
#SBATCH --output=/home/limei/ProtoryNet/Paper/Bert1/200-class/200_s1.out
#SBATCH --partition=owner_fb12
#SBATCH --gpus=a100_80gb:1
source ~/.bashrc 
cd /home/limei/ProtoryNet/Paper/Bert1/200-class
conda activate /home/limei/miniconda3/envs/old-tf
python3 bert_200.py 