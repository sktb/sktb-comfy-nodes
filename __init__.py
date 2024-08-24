from .SKTBMegaBus import SKTBMegaBus
from .SKTBModelBus import SKTBModelBus
from .SKTBPromptBus import SKTBPromptBus
from .SKTBWorkflowInit import SKTBWorkflowInit

NODE_CLASS_MAPPINGS = {
    "SKTBMegaBus": SKTBMegaBus,
    "SKTBModelBus": SKTBModelBus,
    "SKTBPromptBus": SKTBPromptBus,
    "SKTBWorkflowInit": SKTBWorkflowInit,
}

NODE_DISPLAY_NAMES_MAPPINGS = {
    "SKTBMegaBus": "SKTB - Mega Bus",
    "SKTBModelBus": "SKTB - Model Bus",
    "SKTBPromptBus": "SKTB - Prompt Bus",
    "SKTBWorkflowInit": "SKTB - Workflow Initialiser",
}

# WEB_DIRECTORY = "./js"

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAMES_MAPPINGS"]