class AppError(object):

    def exit(self, message):
        print(message)
        exit(1)

ExitError = AppError()
