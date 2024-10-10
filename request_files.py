from fastapi import FastAPI, File, UploadFile
from typing import Annotated

app = FastAPI()


@app.post('/file')
async def file(file: Annotated[list[bytes], File()]):
    return {'file_content': file, 'length': len(file)}


@app.post('/file/upload-file')
async def file(file: Annotated[UploadFile, File()]):
    content = await file.read()
    return {'file_content': content,
            'length': len(content),
            'file_name': file.filename}
