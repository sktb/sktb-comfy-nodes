import comfy.samplers
import folder_paths
import torch

NODE_NAME = "Workflop Initialiser (SKTB)"

REQUIRED_INPUTS = {
    "checkpoint_name": (folder_paths.get_filename_list("checkpoints"), ),
    "clip_last_layer": ("INT", {"default": -1, "min": -24, "max": -1, "step": 1}),
    "image_width": ("INT", {"default": 512, "min": 256, "max": 2048, "step": 128}),
    "image_height": ("INT", {"default": 512, "min": 256, "max": 2048, "step": 128}),
    "batch_count": ("INT", {"default": 1, "min": 1, "max": 16, "step": 1})
}
OPTIONAL_INPUTS = {
}

class SKTBWorkflowInit:
    @classmethod
    def INPUT_TYPES(cls):
        inputs = {
            "required": REQUIRED_INPUTS,
            "optional": OPTIONAL_INPUTS,
        }
        return inputs

    RETURN_TYPES = ("MODEL_BUS", "MODEL", "CLIP", "VAE", "LATENT", "INT", "STRING", "STRING", "INT", "INT")
    RETURN_NAMES = ("model_bus", "model", "clip", "vae", "empty_latent", "clip_last_layer", "checkpoint_name", "checkpoint_path", "image_width", "image_height", )
    FUNCTION = "loadModel"
    CATEGORY = "SKTB"

    @classmethod
    def loadModel(
            self,
            checkpoint_name,
            clip_last_layer,
            image_width,
            image_height,
            batch_count,
        ):

        checkpoint_path = folder_paths.get_full_path("checkpoints", checkpoint_name)
        (model, clip, vae, clip_vision,) = comfy.sd.load_checkpoint_guess_config(checkpoint_path, True, True, True, folder_paths.get_folder_paths("embeddings"))

        clip = clip.clone()
        clip.clip_layer(clip_last_layer)

        device = comfy.model_management.intermediate_device()
        latent = {
            "samples": torch.zeros([batch_count, 4, image_height // 8, image_width // 8], device=device),
        }

        model_bus = {
            "model": model,
            "clip": clip,
            "vae": vae,
            "latent": latent,
        }

        return (model_bus, model, clip, vae, latent, clip_last_layer, checkpoint_name, checkpoint_path, )
