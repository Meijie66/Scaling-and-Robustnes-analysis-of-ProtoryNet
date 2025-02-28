#!/bin/bash
#SBATCH --job-name=50_bert3
#SBATCH --time=6:00:00
#SBATCH --mem=80GB
#SBATCH --error=/home/limei/ProtoryNet/Paper/Bert3/50-class/50_s3.err
#SBATCH --output=/home/limei/ProtoryNet/Paper/Bert3/50-class/50_s3.out
#SBATCH --partition=owner_fb12
#SBATCH --gpus=a100_80gb:1
source ~/.bashrc 
cd /home/limei/ProtoryNet/Paper/Bert3/50-class
conda activate /home/limei/miniconda3/envs/old-tf
python3 bert_50.py 