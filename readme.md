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
        thread_pool_workers=5,
    )
```

## Parameters && Structures

### VideoPart

VideoPart代表投稿内各个分p

path:上传的文件路径

title:分p标题

desc:分p简介

server_file_name:pre_upload API自动生成的服务端文件名，不需要填写


### Upload

parts：VideoPart结构体

copyright: int 版权标志，1为原创2为转载，转载投稿需要填写下面的source参数

title: str 投稿标题

tid: int 投稿分区号

tag: str 以半角逗号分割的字符串

desc: str 视频简介

source: int, 转载地址

cover: int, 封面，TODO（暂时鸽了有时间再做）

no_reprint: int = 0,视频是否禁止转载标志0无1禁止

open_elec: int = 1,是否开启充电面板，0为关闭1为开启

max_retry: int = 5 上传重试次数

thread_pool_workers: int = 1 多视频并行上传最大线程数，默认为串行上传

关于投稿分区tid号码可以从这里查询：
https://github.com/FortuneDayssss/BilibiliUploader/wiki/Bilibili%E5%88%86%E5%8C%BA%E5%88%97%E8%A1%A8

## reference
[记一次B站投稿工具逆向](https://fortunedayssss.github.io/2020/05/20/%E8%AE%B0%E4%B8%80%E6%AC%A1B%E7%AB%99%E6%8A%95%E7%A8%BF%E5%B7%A5%E5%85%B7%E9%80%86%E5%90%91.html). 
