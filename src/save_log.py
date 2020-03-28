# Ω*
#               ■          ■■■■■  
#               ■         ■■   ■■ 
#               ■        ■■     ■ 
#               ■        ■■       
#     ■■■■■     ■        ■■■      
#    ■■   ■■    ■         ■■■     
#   ■■     ■■   ■          ■■■■   
#   ■■     ■■   ■            ■■■■ 
#   ■■■■■■■■■   ■              ■■■
#   ■■          ■               ■■
#   ■■          ■               ■■
#   ■■     ■    ■        ■■     ■■
#    ■■   ■■    ■   ■■■  ■■■   ■■ 
#     ■■■■■     ■   ■■■    ■■■■■


# -- Imports --------------------------------------------------------------------------

from pathlib import Path
from moca_core import N

# -------------------------------------------------------------------------- Imports --

# -- Variables --------------------------------------------------------------------------

log_file_path = str(Path(__file__).parent.parent.joinpath('log').joinpath('BliveCommentAPI.log'))

# -------------------------------------------------------------------------- Variables --

# -- Save Log --------------------------------------------------------------------------


def save_log(log: str) -> None:
    with open(log_file_path, mode='a', encoding='utf-8') as file:
        file.write(log)
        file.write(N)

# -------------------------------------------------------------------------- Save Log --
