## BilibiliUploader
模拟B站pc投稿工具进行投稿

## Example
```
from bilibiliuploader.bilibiliuploader import BilibiliUploader
from bilibiliuploader.core import VideoPart

if __name__ == '__main__':
    uploader = BilibiliUploader()
    uploader.login("username_example", "password_example")

    parts = []
    parts.append(VideoPart(
        path="C:/Users/xxx/Videos/1.mp4",
        title="分p名:p1",
        desc="这里是p1的简介"
    ))
    parts.append(VideoPart(
        path="C:/Users/xxx/Videos/2.mp4",
        title="分p名:p2",
        desc="这里是p2的简介"
    ))
    uploader.upload(
        parts=parts,
        copyright=2,
        title='py多p上传测试1',
        tid=171,
        tag=",".join(["python", "测试"]),
        desc="python多p上传测试",
        source='https://www.github.com/FortuneDayssss',
    )
```

## reference
[记一次B站投稿工具逆向](https://fortunedayssss.github.io/2020/05/20/%E8%AE%B0%E4%B8%80%E6%AC%A1B%E7%AB%99%E6%8A%95%E7%A8%BF%E5%B7%A5%E5%85%B7%E9%80%86%E5%90%91.html). 
