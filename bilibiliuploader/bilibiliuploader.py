import bilibiliuploader.core as core
import bilibiliuploader.util.persist as persist


class BilibiliUploader():
    def __init__(self):
        self.access_token = None
        self.refresh_token = None
        self.sid = None
        self.mid = None

    def login(self, username, password):
        self.access_token, self.refresh_token, self.sid, self.mid = persist.load_login_info()
        print(self.access_token)
        if self.access_token == "":
            self.access_token, self.refresh_token, self.sid, self.mid = core.login(username, password)
            persist.save_login_info(self.access_token, self.refresh_token, self.sid, self.mid)

    def upload(self,
               parts,
               copyright: int,
               title: str,
               tid: int,
               tag: str,
               desc: str,
               source: str = '',
               cover: str = '',
               no_reprint: int = 0,
               open_elec: int = 1,
               max_retry: int = 5,
               thread_pool_workers: int = 1):
        return core.upload(self.access_token,
                    self.sid,
                    self.mid,
                    parts,
                    copyright,
                    title,
                    tid,
                    tag,
                    desc,
                    source,
                    cover,
                    no_reprint,
                    open_elec,
                    max_retry,
                    thread_pool_workers)
