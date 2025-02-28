#!/bin/bash
#SBATCH --job-name=3_bert1
#SBATCH --time=6:00:00
#SBATCH --mem=80GB
#SBATCH --error=/home/limei/ProtoryNet/Paper/Bert1/3-class/3_s1.err
#SBATCH --output=/home/limei/ProtoryNet/Paper/Bert1/3-class/3_s1.out
#SBATCH --partition=owner_fb12
#SBATCH --gpus=a100_80gb:1
source ~/.bashrc 
cd /home/limei/ProtoryNet/Paper/Bert1/3-class
conda activate /home/limei/miniconda3/envs/old-tf
python3 bert_3.py 