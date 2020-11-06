from http import HTTPStatus


class ClientError(Exception):
    def __init__(self, message=None, status_code=None, error_code=None, errors=None):
        self.message = message
        self.status_code = status_code
        self.error_code = error_code
        self.errors = errors

    def __repr__(self):
        return f'<ClientError {self.status_code}: {self.error_code}>'

    def __str__(self):
        message = self.message or self._get_status_description() or 'Unexpected error'
        if self.error_code and self.errors:
            errors = ','.join(self.errors)
            return f'{message}: {self.error_code} - {errors}'
        return message

    def _get_status_description(self):
        if not self.status_code:
            return
        status = HTTPStatus(self.status_code)
        description = status.name.replace('_', ' ').title()
        return f'{self.status_code} {description}'
