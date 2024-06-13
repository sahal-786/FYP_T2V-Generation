import torch
from diffusers import DiffusionPipeline, DPMSolverMultistepScheduler
from diffusers.utils import export_to_video

def generate_video(text_prompt):
    pipe = DiffusionPipeline.from_pretrained("damo-vilab/text-to-video-ms-1.7b", torch_dtype=torch.float16, variant="fp16")
    pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)
    pipe.enable_model_cpu_offload()
    pipe.enable_vae_slicing()

    video_frames = pipe(text_prompt, num_inference_steps=25, num_frames=200).frames

    flattened_frames = []
    for batch in video_frames:
        for frame in batch:
            flattened_frames.append(frame)

    video_path = "static/output_video.mp4" 
    export_to_video(flattened_frames, video_path)
    
    return video_path
