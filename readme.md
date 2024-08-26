
### 项目简介
从ragflow中抽取的ocr部分，再用fastapi简单写了个接口。非官方项目


### 使用

**部署**
```bash
conda create -n ragflow_ocr
conda activate ragflow_ocr

git clone https://github.com/xuxianren/ragflow_ocr.git

pip install -r requirements.txt

uvicorn ragflow_ocr.app:app
```

**使用**

打开[http://localhost:8000/docs](http://localhost:8000/docs)查看接口文档并调试




### 致谢

+ [ragflow](https://github.com/infiniflow/ragflow)

