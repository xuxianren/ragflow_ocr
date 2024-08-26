from typing import Annotated, Union

from fastapi import FastAPI, File
from fastapi.responses import JSONResponse

import io

import numpy as np
from PIL import Image
from .ocr import OCR

ocr = OCR()
app = FastAPI()

@app.post("/ocr")
def rec(file: Annotated[bytes, File()]):
    img = Image.open(io.BytesIO(file)).convert('RGB')
    bxs = ocr(np.array(img))
    txt = "\n".join([t[0] for _, t in bxs if t[0]])
    return JSONResponse(
        content={
            "result": txt
        }
    )

