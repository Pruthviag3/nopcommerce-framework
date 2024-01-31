import logging

class LogGen:
    @staticmethod
    def loggen():
        # logging.basicConfig(filename=".\\Logs\\automation.log",
        #                     format='%(asctime)s - %(levelname)s - %(message)s',datefmt='%m/%d/%y %I:%M:%S %p')
        logging.basicConfig(filename=".\\Logs\\automation.log", level=logging.DEBUG, force=True)
        logger=logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger

