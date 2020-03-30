from . import FILE_SYSTEM_PATH
import json

class FileSystemHandler(object):

    """
    Operates the flow between the models and the file system.
    """

    def __init__(self, file_identifier):
        file_extension = "json"
        self.__file_name = "".join([file_identifier, ".", file_extension])

    # Get data from file system in producton
    # Note: Implement here the access process for particular FTP server
    def retrieve_from_endpoint(self):
        return None

    def set_data_to_endpoint(self, data):
        return None

    # Get the serveable data for the client
    def retrieve_data(self):
        return_data = None
        endpoint_data = self.retrieve_from_endpoint()

        if not endpoint_data:
            f = self.open_file(self.__file_name, "rb")
            data = f.read()
            f.close()

            if len(data) > 0:
                return_data = json.loads(data)

        return return_data

    # Required dict_data format is the following:
    # {
    #  time: {sender_name: message},
    # }
    def set_data(self, dict_data):
        data = json.dumps(dict_data).encode()
        endpoint_set = self.set_data_to_endpoint(data)
        status_code = 500

        if not endpoint_set:
            f = super().open_file(self.__file_name, "wb")
            f.write(data)
            f.close()
            status_code = 200

        return status_code

    @staticmethod
    def open_file(file_name, operation, file_path=FILE_SYSTEM_PATH):
        f = open(file_path+file_name, operation)
        return f
