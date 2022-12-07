from PIL import Image
import torch
from torch import autocast
from tqdm.auto import tqdm
import random
from diffusers import StableDiffusionImg2ImgPipeline, LMSDiscreteScheduler, StableDiffusionPipeline
import os

#from diffusers import StableDiffusionInpaintPipeline
device = "cuda:3"
model_path = "CompVis/stable-diffusion-v1-4"

lms = LMSDiscreteScheduler(
    beta_start=0.00085, 
    beta_end=0.012, 
    beta_schedule="scaled_linear",
    num_train_timesteps=1000
)

pipe = StableDiffusionImg2ImgPipeline.from_pretrained(
    model_path,
    scheduler=lms,
    use_auth_token=True
)
pipe.safety_checker = lambda images, clip_input: (images, False)
pipe = pipe.to(device)
prompt = "High quality rendering of 3D Naruto face" 
#breakpoint()
outdir = 'dummy/00007/'
if not os.path.exists(outdir):
    os.makedirs(outdir)

in_file_path = 'navi10k/'

filelist=os.listdir(in_file_path)

for ib, img_path in enumerate(filelist):
    if ib <= 4000:
        continue
    if ib > 10000:
        break
    if not img_path.endswith(".png"):
        continue
    print(ib)
    init_img = Image.open(in_file_path+img_path).convert("RGB")
    init_img = init_img.resize((512, 512))
    #seed = random.randint(10000, 10000000)
    generator = torch.Generator(device=device).manual_seed(102871)
    with autocast('cuda'):
        image = pipe(prompt=prompt, init_image=init_img, strength=0.60, guidance_scale=12, num_inference_steps=100, generator=generator).images[0]
        image.save(outdir+img_path)