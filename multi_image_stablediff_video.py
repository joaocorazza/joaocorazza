
from stable_diffusion_videos.stable_diffusion_walk import walk

prompt_n_seed = {
    "woman rich and elegant": 743,
    "mansion with stairs": 140,
    "fur coat": 40,
    "short haircut": 560,
    "mansion directly facing camera": 996,
    "woman with letter in the hand": 283,
    "woman rich with three mens in the table on garden": 116,
    "all aesthetich black and white": 277,
}


walk(prompts=list(prompt_n_seed.keys()), 
     seeds=list(prompt_n_seed.values()),
     make_video=True, 
     name="porschevolution",
     num_steps=200,
     use_lerp_for_text=True,
     upscale=True
     )
