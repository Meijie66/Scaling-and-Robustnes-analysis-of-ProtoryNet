#!/bin/bash
#SBATCH --job-name=20_old
#SBATCH --time=1-10:00:00
#SBATCH --mem=80GB
#SBATCH --error=/home/limei/ProtoryNet/old_tf/Number_classes/CUB_20_old/20_s1.err
#SBATCH --output=/home/limei/ProtoryNet/old_tf/Number_classes/CUB_20_old/20_s1.out
#SBATCH --partition=owner_fb12
#SBATCH --gpus=a100_80gb:1
source ~/.bashrc 
cd /home/limei/ProtoryNet/old_tf/Number_classes/CUB_20_old
conda activate /home/limei/miniconda3/envs/old-tf
python3 CUB_20_old.py 