#!/bin/bash
#SBATCH --job-name=10_l5
#SBATCH --time=20:00:00
#SBATCH --mem=80GB
#SBATCH --error=/home/limei/ProtoryNet/old_tf/Learning_rate/CUB_10_l5/10_l5.err
#SBATCH --output=/home/limei/ProtoryNet/old_tf/Learning_rate/CUB_10_l5/10_l5.out
#SBATCH --partition=owner_fb12
#SBATCH --gpus=a100_80gb:1
source ~/.bashrc 
cd /home/limei/ProtoryNet/old_tf/Learning_rate/CUB_10_l5
conda activate /home/limei/miniconda3/envs/old-tf
python3 CUB_10_l5.py 