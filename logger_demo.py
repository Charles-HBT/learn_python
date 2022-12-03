# import logging
# from logging.handlers import RotatingFileHandler
'''
logger:日志器，提供程序可使用的接口
handler：处理器，用于写入日志文件并输出到指定位置，如文件、控制台
filter:过滤器，用于输出符合指定条件的日志记录
formatter：各时期，决定日志记录的输出格式

DEBUG:最低级别，追踪问题时使用
INFO:记录程序中一般事件的信息，或确认一切工作正常
WARNING:记录信息，用于警告
ERROR:用于记录程序报错信息
CRITICAL:最高级别，记录可能导致程序崩溃的错误
'''
# # 创建日志器,
# logger = logging.getLogger()
# # 设置日志级别
# logger.setLevel(logging.DEBUG)
# # 创建处理器对象，指明日志保存的路径、每个日志文件的最大大小、保存的日志文件个数上限
# file_log_handler = RotatingFileHandler("log/test.log", maxBytes=1024 * 1024 * 100, backupCount=10)
# # 创建日志记录的格式
# formatter = logging.Formatter('%(levelname)s %(asctime)s %(filename)s:第%(lineno)d行: %(message)s')
# # 设置日志记录格式
# file_log_handler.setFormatter(formatter)
# stream_handler = logging.StreamHandler()  # 往屏幕上输出
# # 为日志器添加处理方式
# logger.addHandler(file_log_handler)
# logger.addHandler(stream_handler)
# logger.debug("这条日志是debug级别")
# logger.info("这条日志是info级别")
# logger.warning("这条日志是warning级别")
# logger.error("这条日志是error级别")
# logger.critical("这条日志是critical级别")

#优化，封装，方便需要使用时，直接调用，将日志按照日期分别放到不同文件，日志名称以时间命名

import logging,os,time
class Logging():
    def make_log_dir(self,dirname='logs'): #创建日志存放目录，并返回目录的路径
        now_dir=os.path.dirname(__file__)
        # father_path=os.path.split(now_dir)[0]
        path=os.path.join(now_dir,dirname)
        path=os.path.normpath(path) #os.path.normpath()方法规范路径输出格式
        if not os.path.exists(path):
            os.makedirs(path)
        return path

    def get_log_filename(self): #创建文件文件名格式，便于区分每天的日志
        filename="{}.log".format(time.strftime("%Y-%m-%d",time.localtime()))
        filename=os.path.join(self.make_log_dir(),filename)
        filename=os.path.normpath(filename)
        return filename

    def log(self,level='DEBUG'): #生成日志的主方法，传入对哪些级别以上的日志进行处理
        logger=logging.getLogger()
        logger.setLevel(level)
        if not logger.handlers:
            sh=logging.StreamHandler()
            fh=logging.FileHandler(filename=self.get_log_filename(),mode='a',encoding="utf-8")
            fmt=logging.Formatter("%(asctime)s-%(levelname)s-%(filename)s-line:%(lineno)d-message:%(message)s")
            sh.setFormatter(fmt=fmt)
            fh.setFormatter(fmt=fmt)
            logger.addHandler(fh)
            logger.addHandler(sh)
        return logger
if __name__=='__main__':
    logger=Logging().log(level="ERROR")
    logger.debug("debug-111111")
    logger.info("info-2222222")
    logger.error("error-333333")
    logger.warning("warning-4444444")
    logger.critical("critical-555555")
