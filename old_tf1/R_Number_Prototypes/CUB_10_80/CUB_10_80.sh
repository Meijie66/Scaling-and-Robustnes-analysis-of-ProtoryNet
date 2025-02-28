#!/bin/bash
#SBATCH --job-name=R_10_80
#SBATCH --time=1-10:00:00
#SBATCH --mem=80GB
#SBATCH --error=/home/limei/ProtoryNet/old_tf1/R_Number_Prototypes/CUB_10_80/R_10_80.err
#SBATCH --output=/home/limei/ProtoryNet/old_tf1/R_Number_Prototypes/CUB_10_80/R_10_80.out
#SBATCH --partition=owner_fb12
#SBATCH --gpus=a100_80gb:1
source ~/.bashrc 
cd /home/limei/ProtoryNet/old_tf1/R_Number_Prototypes/CUB_10_80
conda activate /home/limei/miniconda3/envs/old-tf
python3 CUB_10_80.py 