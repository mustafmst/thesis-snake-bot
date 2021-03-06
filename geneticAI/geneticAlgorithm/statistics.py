import datetime
import json
import os


class AlgorithmStatistics:
    """
        TODO:
        Make new folder for each run logs
    """
    FOLDER_NAME = "logs"
    MODEL_SUFFIX = "-model"
    RESULT_SUFFIX = "-results"
    CONFIG_SUFFIX = "-game_config"

    def __init__(self, config):
        self.__config = config
        self.__prefix = "{}_pop{}_gen{}_mut{}".format(
            datetime.datetime.now().strftime("%Y%m%d:%H:%M"),
            config["population_size"],
            config["generations"],
            config["generation_mutation_rate"]
        )
        self.__stats = []
        if not os.path.isdir(os.path.join(os.getcwd(), self.FOLDER_NAME)):
            os.mkdir(os.path.join(os.getcwd(), self.FOLDER_NAME))

    def save_model(self, candidate):
        if candidate is not None:
            candidate.save_model(os.path.join(os.getcwd(),
                                              self.FOLDER_NAME,
                                              '{}{}.h5'.format(
                                                  self.__prefix,
                                                  self.MODEL_SUFFIX)))
        with open(os.path.join(
            os.getcwd(),
            self.FOLDER_NAME,
            '{}{}.json'.format(
                self.__prefix,
                self.CONFIG_SUFFIX
            )
        ), 'w') as config_file:
            to_save = {
                'board': self.__config["base_game_config"]["board_size"],
                'network': self.__config["network_schema"]
            }
            json.dump(to_save, config_file, indent=4)
        pass

    def log_generation_result(self, best_result, generation):
        self.__stats.append(
            dict(
                time=str(datetime.datetime.now()),
                result=best_result,
                generation=generation
            )
        )
        with open(os.path.join(os.getcwd(),
                               self.FOLDER_NAME,
                               '{}{}.json'.format(
                                   self.__prefix,
                                   self.RESULT_SUFFIX)),
                  'w') as result_file:
            json.dump(self.__stats, result_file, indent=4)
